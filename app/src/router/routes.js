import login from '@/views/loginView/LoginView';
import signup from '@/views/signupView/SignupView';
import programDetail from '@/views/programDetailView/ProgramDetailView';
import ProfileView from '@/views/profileView/ProfileView';
import TrainPrograms from '@/views/trainProgramsView/TrainProgramsView';
import PageInDevelopment from '@/views/pageInDevelopmentView/PageInDevelopmentView';
import NotFound from '@/views/notFoundView/NotFoundView';

export const routes = [
	{
		path: '/login',
		name: 'LoginPage',
		component: login,
	},
	{
		path: '/signup',
		name: 'SignupPage',
		component: signup,
	},
	{
		path: '/profile',
		name: 'ProfilePage',
		component: ProfileView,
	},
	{
		path: '/train-programs',
		name: 'TrainProgramsPage',
		component: TrainPrograms,
	},
	{
		path: '/train-programs/:id',
		name: 'programDetailView',
		component: programDetail,
	},
	{
		path: '/',
		name: 'PageInDevelopment',
		component: PageInDevelopment,
	},
	{
		path: '/:catchAll(.*)',
		name: 'NotFound',
		component: NotFound,
	},
];
