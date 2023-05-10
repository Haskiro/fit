import login from "@/views/loginView/LoginView"
import signup from "@/views/signupView/SignupView"
import programDetail from "@/views/programDetailView/ProgramDetailView"

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
  {
    path: "/program",
    name: "programDetailView",
    component: programDetail
  },
];
