import React from "react";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import darkTheme from "./mui-dark";

// Default implementation, that you can customize
export default function Root({ children }) {
  return (
    <ThemeProvider theme={darkTheme}>
      <>{children}</>
    </ThemeProvider>
  );
}
