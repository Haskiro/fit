import login from "../views/LoginView"
import signup from "../views/SignupView"

export const routes = [
  {
    path: "/login",
    name: "LoginPage",
    component: login
  },
  {
    path: "/signup",
    name: "SignupPage",
    component: signup
  },
];
