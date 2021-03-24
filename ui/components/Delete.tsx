import styled from "@emotion/styled";

export const Delete = styled.button`
  &::after {
    content: "✕";
  }
  border: 0;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  padding: 3px;
  background-color: hotpink;
  opacity: 0.8;
  font-size: 16px;
  height: 24px;
  width: 24px;
  border-radius: 12px;
  cursor: pointer;
  color: white;
  flex: none;

  &:hover {
    box-shadow: none;
    opacity: 1;
  }
  &:active {
    outline: 0;
  }
`;
