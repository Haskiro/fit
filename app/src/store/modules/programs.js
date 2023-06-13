import programsApi from '@/api/programs';
import { _mapProgramInfo, _transformProgramListItem } from '@/utils/transformProgram';
import { PROGRAMS_COMPLEXITY } from '@/consts/maps';

export const programsModule = {
	state: () => ({
		programs: [],
		checkedProgram: {},
	}),
	mutations: {
		setPrograms(state, newPrograms) {
			state.programs = newPrograms;
		},
		setCheckedProgram(state, program) {
			state.checkedProgram = program;
		},
	},
	actions: {
		async fetchAllPrograms({ commit }) {
			const res = await programsApi.getPrograms();
			const programs = res.map((program) => _transformProgramListItem(program));
			commit('setPrograms', programs);
		},
		async fetchProgramById({ commit }, id) {
			const res = await programsApi.getProgramById(id);
			const program = _mapProgramInfo(res);
			commit('setCheckedProgram', program);
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
