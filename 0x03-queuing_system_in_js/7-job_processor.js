import kue from 'kue';

const queue = kue.createQueue();

const blackListedPhone = ['4153518780', '4153518781'];

function sendNotification (phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blackListedPhone.includes(phoneNumber)) {
    return (done(new Error(`Phone muner ${phoneNumber} is blacklisted`)));
  }
  
  job.progress(50, 100);

  job.on('progress', (progress, data) => {
    console.log(`Sending notification to ${data.phoneNumber} with message: ${data.message}`);
  });

  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  done();
}

queue.process('push_notification_code_2', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
