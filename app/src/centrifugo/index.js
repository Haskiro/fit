import { Centrifuge } from 'centrifuge';

const centrifuge = new Centrifuge('ws://localhost:8002/connection/websocket', {
	token: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSIsImV4cCI6MTY4NzcyNjcwMiwiaWF0IjoxNjg3MTIxOTAyfQ.vb4hvrTTjmYwE6_C8f49SOCx6TrCk3Hzwc16l-9mQz0',
});

centrifuge
	.on('connecting', function (ctx) {
		console.log(`connecting: ${ctx.code}, ${ctx.reason}`);
	})
	.on('connected', function (ctx) {
		console.log(`connected over ${ctx.transport}`);
	})
	.on('disconnected', function (ctx) {
		console.log(`disconnected: ${ctx.code}, ${ctx.reason}`);
	});

const sub = centrifuge.newSubscription('channel');

sub.on('subscribing', function () {
	console.log('subscribing');
});

sub.on('subscribed', function () {
	console.log('subscribed');
});

sub.on('unsubscribed', function () {
	console.log('unsubscribed');
});

export { centrifuge, sub };
