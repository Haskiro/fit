import { createStore } from 'vuex';
import { programsModule } from './modules/programs';
import auth from './modules/auth';

const debug = process.env.NODE_ENV !== 'production';

const store = createStore({
	modules: {
		programs: programsModule,
		auth,
	},
	strict: debug,
});

export default store;
