import createPushNotificationsJobs from "./8-jobs.js";
import kue from 'kue';
import { expect } from "chai";
import { describe, it, before, after, afterEach } from "mocha";


describe('createPushNotification', () => {    
    const queue = kue.createQueue();
    before(() => {
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
    })

    after(() => {
        queue.testMode.exit();
    });

    const jobArray = [
        {
          phoneNumber: '4153518780',
          message: 'This is the code 1234 to verify your account'
        },
        {
          phoneNumber: '4153518781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4153518743',
          message: 'This is the code 4321 to verify your account'
        },
        {
          phoneNumber: '4153538781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4153118782',
          message: 'This is the code 4321 to verify your account'
        },
        {
          phoneNumber: '4153718781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4159518782',
          message: 'This is the code 4321 to verify your account'
        },
        {
          phoneNumber: '4158718781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4153818782',
          message: 'This is the code 4321 to verify your account'
        },
        {
          phoneNumber: '4154318781',
          message: 'This is the code 4562 to verify your account'
        },
        {
          phoneNumber: '4151218782',
          message: 'This is the code 4321 to verify your account'
        }
    ];

    it ('display a error message if jobs is not an array', () => {
        const result = createPushNotificationsJobs(12345, queue);
        expect(result).to.be.an.instanceOf(Error);
        expect(result.message).to.equal('Jobs is not an Array');
    });

    it ('should add jobs to the queue', () => {
        createPushNotificationsJobs(jobArray, queue);
        expect(queue.testMode.jobs.length).to.equal(jobArray.length);
        expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3')
    });
})