import kue from 'kue';

const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
	phoneNumber: "",
	message: "",
	}).save( function( err ){
		if( !err ) console.log(`Notification job created: ${job.id}`);
	});

job.on('complete', (result) => {
	console.log('Notification job completed');

}).on('failed', (errMessage) => {
	console.log('Notification job failed');
});
