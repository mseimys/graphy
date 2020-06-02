import * as React from "react";
import gql from "graphql-tag";
import { useQuery, useMutation } from "@apollo/react-hooks";

import { Delete } from "./Delete";
import { Container } from "./Container";

const CategoryListPage = {
  fragments: {
    category: gql`
      fragment CategoryParts on Category {
        id
        name
      }
    `,
  },
};

const CATEGORY_LIST = gql`
  {
    categories(limit: 100) {
      ...CategoryParts
    }
  }
  ${CategoryListPage.fragments.category}
`;

const ADD_CATEGORY = gql`
  mutation CreateCategory($name: String!) {
    createCategory(name: $name) {
      ...CategoryParts
    }
  }
  ${CategoryListPage.fragments.category}
`;

const DELETE_CATEGORY = gql`
  mutation DeleteCategory($id: ID!) {
    deleteCategory(id: $id)
  }
`;

const CATEGORY_SUBSCRIPTION = gql`
  subscription onCategoryAdded {
    categoryAdded {
      id
      name
    }
  }
`;

export function CategoryList() {
  const { loading, error, data } = useQuery(CATEGORY_LIST);
  const [name, setName] = React.useState("");
  const [addCategory] = useMutation(ADD_CATEGORY, {
    // refetchQueries: [{ query: CATEGORY_LIST }],
    // But... instead of refetching, let's update cache with received data
    update(cache, { data: { createCategory } }) {
      const { categories } = cache.readQuery({ query: CATEGORY_LIST });
      cache.writeQuery({
        query: CATEGORY_LIST,
        data: { categories: [createCategory, ...categories] },
      });
    },
  });
  const [deleteCategory] = useMutation(DELETE_CATEGORY, {
    refetchQueries: [{ query: CATEGORY_LIST }],
  });

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  const handleAdd = async () => {
    const result = await addCategory({
      variables: { name },
      // This is a temporary "optimistic response" that is used immediately (can be seen flashing)
      optimisticResponse: {
        __typename: "Mutation",
        createCategory: {
          __typename: "Category",
          id: "??",
          name: `Ehm..... ${name}`,
        },
      },
    });
    console.log("ADDED", result.data);
  };

  const handleDelete = async (id: string) => {
    const result = await deleteCategory({ variables: { id } });
    console.log("DELETED", result.data);
  };

  console.log("Render", data.categories);
  return (
    <Container>
      <h1>Categories</h1>
      <div>
        <input
          type="text"
          value={name}
          onChange={(e: any) => setName(e.target.value)}
        />
        <button onClick={handleAdd}>Add</button>
      </div>
      <div>
        <ul>
          {data.categories.map(({ id, name }: any) => (
            <li key={id}>
              <p>
                {id}: {name} <Delete onClick={() => handleDelete(id)} />
              </p>
            </li>
          ))}
        </ul>
      </div>
    </Container>
  );
}
