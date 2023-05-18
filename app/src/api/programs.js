import axios from 'axios';

const getPrograms = async () => {
	try {
		const { data } = await axios.get(`${process.env.VUE_APP_API_URL}programs`);
		return data;
	} catch (e) {
		console.log(e.message);
	}
};

const getProgramsById = async (id) => {
	await axios
		.get(`${process.env.VUE_APP_API_URL}programs/${id}`)
		.then((response) => {
			return response.data;
		})
		.catch((error) => {
			console.log(error);
		});
};

export default {
	getPrograms,
	getProgramsById,
};
