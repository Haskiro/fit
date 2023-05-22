import { createStore } from 'vuex';
import { programsModule } from './modules/programs';

const debug = process.env.NODE_ENV !== 'production';

const store = createStore({
	modules: {
		programs: programsModule,
	},
	strict: debug,
});

export default store;
