# GraphQL Testbed

Uses [Ariadne](https://ariadnegraphql.org/) for schema-first GraphQL.

## Queries

```
{
  category(id: 4) {
    id
    name
  }
}
```

```
{
  ingredients(limit: 10) {
    id
    name
    category {
      id
      name
    }
  }
}
```

## Mutations

```
mutation {
  createCategory(name: "Abrakadabra") {
    id
    name
  }
}
```

```
mutation createIngredient($input: IngredientInput!){
  createIngredient(input: $input) {
    id
    name
  }
}

# Pass variables

{
  "input": {
    "name": "Beer",
    "categoryId": "5"
  }
}
```
