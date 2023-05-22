export const _transformProgramListItem = (program) => {
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
