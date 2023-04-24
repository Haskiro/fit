import login from "@/views/loginView/LoginView"
import signup from "@/views/signupView/SignupView"

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
