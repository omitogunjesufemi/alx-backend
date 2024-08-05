function createPushNotificationsJobs (jobs, queue) {
 if (Array.isArray(jobs) === false) {
    throw new Error('Jobs is not an Array');
 }

 for (const jobData of jobs) {
    const job = queue.create('push_notification_code_3', jobData).save((err) => {
        if (err) {
            console.log(`Notification job ${job.id} failed: ${err}`);
        } else {
            console.log(`Notification job created: ${job.id}`);
        }
    });

    job.on('complete', () => {
        console.log(`Notification ${job.id} completed`);
    });

    job.on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
    });

    job.on('progress', (progress, data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
    });
 }
}

export default createPushNotificationsJobs;