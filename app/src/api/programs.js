import axios from 'axios';

const getPrograms = async () => {
	try {
		const { data } = await axios.get(`${process.env.VUE_APP_API_URL}programs`);
		return data;
	} catch (e) {
		console.log(e.message);
	}
};

const getProgramById = async (id) => {
	try {
		const { data } = await axios.get(`${process.env.VUE_APP_API_URL}programs/${id}`);
		return data;
	} catch (e) {
		console.log(e.message);
	}
};

export default {
	getPrograms,
	getProgramById,
};
