import axios from 'axios';
// import { getUser } from '@/api/user';
const state = {
	accessToken: localStorage.getItem('access_token') || null,
	refreshToken: localStorage.getItem('refresh_token') || null,
	status: '',
	user: null,
};

const getters = {
	isLoggedIn: (state) => !!state.accessToken,
	authStatus: (state) => state.status,
	currentUser: (state) => state.user,
};
export function getUser() {
	return axios.get(`${process.env.VUE_APP_API_URL}auth/me/`);
}

const actions = {
	// Авторизация
	login({ commit }, user) {
		return new Promise((resolve, reject) => {
			commit('auth_request');
			axios({
				url: `${process.env.VUE_APP_API_URL}auth/login/`,
				method: 'POST',
				data: user,
			})
				.then((response) => {
					const accessToken = response.data.access;
					const refreshToken = response.data.refresh;
					localStorage.setItem('access_token', accessToken);
					localStorage.setItem('refresh_token', refreshToken);
					axios.defaults.headers.common['Authorization'] = 'Bearer ' + accessToken;
					commit('auth_success', accessToken, refreshToken);
					getUser()
						.then((userResponse) => {
							const user = userResponse.data;
							commit('set_user', user); // Сохраняем данные о пользователе в состояние
						})
						.catch((error) => {
							console.error(error);
						});
					resolve(response);
				})
				.catch((error) => {
					commit('auth_error');
					localStorage.removeItem('access_token');
					localStorage.removeItem('refresh_token');
					reject(error);
				});
		});
	},
	// Регистрация
	register(data) {
		debugger;
		return new Promise((resolve, reject) => {
			axios({
				url: `${process.env.VUE_APP_API_URL}auth//`,
				method: 'POST',
				data: data,
			})
				.then((response) => {
					resolve(response);
				})
				.catch((error) => {
					reject(error);
				});
		});
	},
	// Выход
	logout({ commit }) {
		return new Promise((resolve) => {
			commit('logout');
			localStorage.removeItem('access_token');
			localStorage.removeItem('refresh_token');
			delete axios.defaults.headers.common['Authorization'];
			resolve();
		});
	},
	// Обновление токенов
	refreshTokens({ commit, state }) {
		return new Promise((resolve, reject) => {
			axios({
				url: '',
				method: 'POST',
				data: { refresh: state.refreshToken },
			})
				.then((response) => {
					const accessToken = response.data.access;
					localStorage.setItem('access_token', accessToken);
					axios.defaults.headers.common['Authorization'] = 'Bearer ' + accessToken;
					commit('refresh_success', accessToken);
					resolve(response);
				})
				.catch((error) => {
					commit('auth_error');
					localStorage.removeItem('access_token');
					localStorage.removeItem('refresh_token');
					reject(error);
				});
		});
	},
};

const mutations = {
	auth_request(state) {
		state.status = 'loading';
	},
	auth_success(state, accessToken, refreshToken) {
		state.accessToken = accessToken;
		state.refreshToken = refreshToken;
		state.status = 'success';
	},
	auth_error(state) {
		state.status = 'error';
	},
	logout(state) {
		state.status = '';
		state.accessToken = null;
		state.refreshToken = null;
		state.user = null;
	},
	refresh_success(state, newAccessToken) {
		state.accessToken = newAccessToken;
	},
	set_user(state, user) {
		// Добавляем мутацию для сохранения данных о пользователе в состояние
		state.user = user;
		debugger;
	},
};

export default {
	state,
	getters,
	actions,
	mutations,
};
