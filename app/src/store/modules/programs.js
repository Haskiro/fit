import programsApi from '@/api/programs';
import { _transformProgramListItem } from '@/utils/transformProgramListItem';

export const programsModule = {
	state: () => ({
		programs: [],
	}),
	mutations: {
		setPrograms(state, newPrograms) {
			state.programs = newPrograms;
		},
	},
	actions: {
		async fetchAllPrograms({ commit }) {
			const res = await programsApi.getPrograms();
			const programs = res.map((program) => _transformProgramListItem(program));
			commit('setPrograms', programs);
		},
	},
	getters: {
		sortProgramsByComplexity: (state) => (dir) => {
			return state.programs.sort((a, b) => {
				if (dir === 'up') {
					return PROGRAMS_COMPLEXITY[a] - PROGRAMS_COMPLEXITY[b];
				}
				return PROGRAMS_COMPLEXITY[b] - PROGRAMS_COMPLEXITY[a];
			});
		},
		sortProgramsByNewness: (state) => {
			return state.programs.sort((a, b) => {
				if (a.isNew && !b.isNew) return 1;
				if (!a.isNew && b.isNew) return -1;
				return 0;
			});
		},
		searchProgramsByTitle: (state) => (str) => {
			return state.programs.filter((program) => program.title.toLowerCase().includes(str.toLowerCase()));
		},
	},
	namespaced: true,
};

const PROGRAMS_COMPLEXITY = {
	['Новичок']: 1,
	['Любитель']: 2,
	['Профессионал']: 3,
};
