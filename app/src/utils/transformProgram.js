import { PROGRAMS_INFO_MAP } from '@/consts/maps';

const _transformProgramListItem = (program) => {
	return {
		id: program.id,
		bgImage: process.env.VUE_APP_HOST + program.photo_thumbnail,
		title: program.title,
		goal: program.target,
		bodyType: program.body_type,
		difficulty: program.complexity,
		isNew: (new Date().getDate() - new Date(program.updated_at)) / 1000 / 60 / 60 / 24 < 30,
	};
};

const _mapProgramInfo = (program) => {
	const info = [];
	const mappedProgram = {};

	Object.keys(program).forEach((key) => {
		if (!PROGRAMS_INFO_MAP.has(key)) {
			if (key === 'photo' || key === 'photo_thumbnail') {
				mappedProgram[key] = process.env.VUE_APP_HOST + program[key];
				return;
			}
			mappedProgram[key] = program[key];
			return;
		}
		info.push({ title: PROGRAMS_INFO_MAP.get(key), description: program[key] });
	});
	mappedProgram.info = info;
	return mappedProgram;
};

export { _transformProgramListItem, _mapProgramInfo };
