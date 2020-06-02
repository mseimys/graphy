import * as React from "react";
import gql from "graphql-tag";
import { useQuery } from "@apollo/react-hooks";

const CATEGORY_LIST = gql`
  {
    categories {
      id
      name
    }
  }
`;

export function CategoryList() {
  const { loading, error, data } = useQuery(CATEGORY_LIST);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error :(</p>;

  return (
    <div>
      <h1>Categories</h1>
      <div>
        <ul>
          {data.categories.map(({ id, name }: any) => (
            <li key={id}>
              <p>
                {id}: {name}
              </p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
