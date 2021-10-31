import styled from "@emotion/styled";

export const Title = styled.h1`
  text-align: center;
  color: hotpink;
  font-family: sans-serif;
`;

export const Input = styled.input`
  flex-grow: 1;
  border: 1px solid hotpink;
  line-height: 24px;
  padding: 8px 16px;

  &:active {
    outline: 0;
  }
`;

export const Button = styled.button`
  border: 0;
  line-height: 24px;
  padding: 8px 16px;
  background-color: hotpink;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.2);
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
  color: white;
  opacity: 0.8;
  transition: 0.3s;

  &:hover {
    box-shadow: none;
    opacity: 1;
  }
`;

export const RowBlock = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;

  & > *:not(:last-child) {
    margin-right: 24px;
  }
`;
