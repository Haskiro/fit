import axios from 'axios';
import store from '@/store';

// создаем экземпляр axios с заданными параметрами
export const HTTP = axios.create({
	baseURL: '/api/',
	headers: {
		'Content-Type': 'application/json',
	},
});

HTTP.interceptors.request.use(
	(config) => {
		const accessToken = localStorage.getItem('access_token');
		if (accessToken) {
			config.headers.Authorization = `Bearer ${accessToken}`;
		}
		return config;
	},
	(error) => Promise.reject(error),
);

HTTP.interceptors.response.use(
	(response) => response,
	(error) => {
		return new Promise((resolve, reject) => {
			const originalRequest = error.config;
			if (error.response.status === 401 && !originalRequest._retry) {
				originalRequest._retry = true;
				// const state = store.state.auth;
				// const refresh = state.refreshToken;
				store
					.dispatch('refreshTokens')
					.then((response) => {
						const newAccessToken = response.data.access;
						const newRefreshToken = response.data.refresh;
						localStorage.setItem('access_token', newAccessToken);
						localStorage.setItem('refresh_token', newRefreshToken);
						axios.defaults.headers.common['Authorization'] = `Bearer ${newAccessToken}`;
						originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;
						resolve(axios(originalRequest));
					})
					.catch((error) => {
						store.dispatch('logout');
						reject(error);
					});
			}
			reject(error);
		});
	},
);
