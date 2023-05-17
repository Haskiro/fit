module.exports = {
	root: true,
	env: {
		browser: true,
		node: true,
	},
	extends: ['plugin:vue/recommended', 'eslint:recommended', 'plugin:prettier/recommended'],
	plugins: ['prettier'],
	rules: {
		'prettier/prettier': [
			'error',
			{
				trailingComma: 'all',
				bracketSpacing: true,
				endOfLine: 'auto',
				semi: true,
				singleQuote: true,
				tabWidth: 4,
				printWidth: 120,
				useTabs: true,
			},
		],
		'vue/component-name-in-template-casing': ['error', 'PascalCase'],
		'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
		'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
		'vue/require-default-prop': 'off',
		'vue/comment-directive': 'off',
	},
	globals: {
		_: true,
	},
};
