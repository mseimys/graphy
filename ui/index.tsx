import * as React from "react";
import * as ReactDOM from "react-dom";
import { ApolloProvider } from "@apollo/react-hooks";

import { client } from "./client";
import { CategoryList } from "./components/CategoryList";

function App() {
  return (
    <ApolloProvider client={client}>
      <CategoryList />
    </ApolloProvider>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
