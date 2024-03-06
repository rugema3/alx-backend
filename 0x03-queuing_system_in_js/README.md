<h1>0x03-queuing_system_in_js</h1>
<img src="redis.png">
<h1>Resources</h1>
<li><a href="https://intranet.alxswe.com/rltoken/8xeApIhnxgFZkgn54BiIeA">Redis quick start</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/1rq3ral-3C5O1t67dbGcWg">Redis client interface</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/mRftfl67BrNvl-RM5JQfUA">Redis client for Node JS</a></li>
<li><a href="https://intranet.alxswe.com/rltoken/yTC3Ci2IV2US24xJsBfMgQ">Kue</a> deprecated but still use in the industry</li>

<h2>Required Files for the Project</h2>
<b>package.json</b>
<pre>
{
    "name": "queuing_system_in_js",
    "version": "1.0.0",
    "description": "",
    "main": "index.js",
    "scripts": {
      "lint": "./node_modules/.bin/eslint",
      "check-lint": "lint [0-9]*.js",
      "test": "./node_modules/.bin/mocha --require @babel/register --exit",
      "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    },
    "author": "",
    "license": "ISC",
    "dependencies": {
      "chai-http": "^4.3.0",
      "express": "^4.17.1",
      "kue": "^0.11.6",
      "redis": "^2.8.0"
    },
    "devDependencies": {
      "@babel/cli": "^7.8.0",
      "@babel/core": "^7.8.0",
      "@babel/node": "^7.8.0",
      "@babel/preset-env": "^7.8.2",
      "@babel/register": "^7.8.0",
      "eslint": "^6.4.0",
      "eslint-config-airbnb-base": "^14.0.0",
      "eslint-plugin-import": "^2.18.2",
      "eslint-plugin-jest": "^22.17.0",
      "nodemon": "^2.0.2",
      "chai": "^4.2.0",
      "mocha": "^6.2.2",
      "request": "^2.88.0",
      "sinon": "^7.5.0"
    }
  }
</pre>
<br>
<b>.babelrc</b>
<pre> 
{
  "presets": [
    "@babel/preset-env"
  ]
}
</pre>
<br>
<p>and… Don’t forget to run <b>$ npm install</b> when you have the <b>package.json</b></p>
<h1>Tasks</h1>
<b>0. Install a redis instance</b>
<p>Download, extract, and compile the latest stable Redis version (higher than 5.0.7 - https://redis.io/download/):</p>
<br>
<pre>
$ wget http://download.redis.io/releases/redis-6.0.10.tar.gz
$ tar xzf redis-6.0.10.tar.gz
$ cd redis-6.0.10
$ make
</pre>
<br>
<li>Start Redis in the background with <b>src/redis-server</b></li>

<pre>
$ src/redis-server &
</pre>
<li>Make sure that the server is working with a ping src/redis-cli ping</li>
<pre>PONG</pre>
<li>Using the Redis client again, set the value School for the key Holberton</li>
<pre>
127.0.0.1:[Port]> set Holberton School
OK
127.0.0.1:[Port]> get Holberton
"School"
</pre>
<br>
<li>Kill the server with the process id of the redis-server (hint: use ps and grep)</li>
<pre>$ kill [PID_OF_Redis_Server]</pre>
<p>Copy the dump.rdb from the redis-5.0.7 directory into the root of the Queuing project.</p>

<p>Requirements:</p>

<li>Running get Holberton in the client, should return School</li>
<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: README.md, dump.rdb</li>
  
<b>1. Node Redis Client</b>

Install <a href="https://intranet.alxswe.com/rltoken/mRftfl67BrNvl-RM5JQfUA">node_redis</a> using npm

<p>Using Babel and ES6, write a script named 0-redis_client.js. It should connect to the Redis server running on your machine:</p>

<li>It should log to the console the message Redis client connected to the server when the connection to Redis works correctly</li>
<li>It should log to the console the message Redis client not connected to the server: ERROR_MESSAGE when the connection to Redis does not work</li>
<b>Requirements:</b>

<li>To import the library, you need to use the keyword import</li>
<pre>
bob@dylan:~$ ps ax | grep redis-server
 2070 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$ 
bob@dylan:~$ npm run dev 0-redis_client.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
^C
bob@dylan:~$ 
bob@dylan:~$ ./src/redis-server > /dev/null 2>&1 &
[1] 2073
bob@dylan:~$ ps ax | grep redis-server
 2073 pts/0    Sl     0:00 ./src/redis-server *:6379
 2078 pts/1    S+     0:00 grep --color=auto redis-server
bob@dylan:~$
bob@dylan:~$ npm run dev 0-redis_client.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "0-redis_client.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 0-redis_client.js`
Redis client connected to the server
^C
bob@dylan:~$
</pre>
<br>
<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 0-redis_client.js</li>
  
<b>2. Node Redis client and basic operations</b>
<p>
In a file 1-redis_op.js, copy the code you previously wrote (0-redis_client.js).
</p>
<p>Add two functions:</p>

<li>setNewSchool:
  <li>It accepts two arguments schoolName, and value.</li>
  <li>It should set in Redis the value for the key schoolName</li>
  <li>It should display a confirmation message using redis.print</li>
</li>
<li>displaySchoolValue:
  <li>It accepts one argument schoolName.</li>
  <li>It should log to the console the value for the key passed as argument</li>
</li>
<p>At the end of the file, call:</p>

<li>displaySchoolValue('Holberton');</li>
<li>setNewSchool('HolbertonSanFrancisco', '100');</li>
<li>displaySchoolValue('HolbertonSanFrancisco');</li>
<b>Requirements:</b>

<li>Use callbacks for any of the operation, we will look at async operations later</li>
<pre>
bob@dylan:~$ npm run dev 1-redis_op.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "1-redis_op.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 1-redis_op.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$
</pre><br>

<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 1-redis_op.js</li>
  
<b>3. Node Redis client and async operations</b>
<p>In a file 2-redis_op_async.js, let’s copy the code from the previous exercise (1-redis_op.js)</p>

<p>Using promisify, modify the function displaySchoolValue to use ES6 async / await</p>

<p>Same result as 1-redis_op.js</p>
<pre>
bob@dylan:~$ npm run dev 2-redis_op_async.js

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "2-redis_op_async.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 2-redis_op_async.js`
Redis client connected to the server
School
Reply: OK
100
^C

bob@dylan:~$
</pre><br>
<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 2-redis_op_async.js</li>
  
<b>4. Node Redis client and advanced operations</b>
<p>
In a file named 4-redis_advanced_op.js, let’s use the client to store a hash value</p>

<b>Create Hash:</b>
<p>Using hset, let’s store the following:</p>

<li>The key of the hash should be HolbertonSchools</li>
<li>It should have a value for:
  <li>Portland=50</li>
  <li>Seattle=80</li>
  <li>New York=20</li>
  <li>Bogota=20</li>
  <li>Cali=40</li>
  <li>Paris=2</li>
</li>
<li>Make sure you use redis.print for each hset</li>
<b>Display Hash:</b>
<p>Using hgetall, display the object stored in Redis. It should return the following:</p>

<b>Requirements:</b>

<p>Use callbacks for any of the operation, we will look at async operations later</p>
<pre>
bob@dylan:~$ npm run dev 4-redis_advanced_op.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "4-redis_advanced_op.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 4-redis_advanced_op.js`
Redis client connected to the server
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
Reply: 1
{
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2'
}
^C
bob@dylan:~$
</pre><br>
<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 4-redis_advanced_op.js</li>
  
<b>5. Node Redis client publisher and subscriber</b>

<p>In a file named 5-subscriber.js, create a redis client:</p>

<li>On connect, it should log the message Redis client connected to the server</li>
<li>On error, it should log the message Redis client not connected to the server: ERROR MESSAGE</li>
<li>It should subscribe to the channel holberton school channel</li>
<li>When it receives message on the channel holberton school channel, it should log the message to the console</li>
<li>When the message is KILL_SERVER, it should unsubscribe and quit</li>
<p>In a file named 5-publisher.js, create a redis client:</p>

<li>On connect, it should log the message Redis client connected to the server</li>
<li>On error, it should log the message Redis client not connected to the server: ERROR MESSAGE</li>
<li>Write a function named publishMessage:
  <li>It will take two arguments: message (string), and time (integer - in ms)</li>
  <li>After time millisecond:
    <li>The function should log to the console About to send MESSAGE</li>
    <li>The function should publish to the channel holberton school channel, the message passed in argument after the time passed in arguments</li>
  </li>
</li>
<li>At the end of the file, call:</li>
<pre>
publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
</pre>
<b>Requirements:</b>

<li>You only need one Redis server to execute the program</li>
<li>You will need to have two node processes to run each script at the same time</li>
<br>
<b>Terminal 1:</b>
<pre>
bob@dylan:~$ npm run dev 5-subscriber.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "5-subscriber.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-subscriber.js`
Redis client connected to the server
</pre><br>
<b>Terminal 2:</b>
<pre>
bob@dylan:~$ npm run dev 5-publisher.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "5-publisher.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 5-publisher.js`
Redis client connected to the server
About to send Holberton Student #1 starts course
About to send Holberton Student #2 starts course
About to send KILL_SERVER
About to send Holberton Student #3 starts course
^C
bob@dylan:~$ 
</pre>
<b>And in the same time in Terminal 1:</b>
<pre>
Redis client connected to the server
Holberton Student #1 starts course
Holberton Student #2 starts course
KILL_SERVER
[nodemon] clean exit - waiting for changes before restart
^C
bob@dylan:~$ 
</pre>
<p>Now you have a basic Redis-based queuing system where you have a process to generate job and a second one to process it. These 2 processes can be in 2 different servers, which we also call “background workers”.
</p>
<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 5-subscriber.js, 5-publisher.js</li>
  
<b>6. Create the Job creator</b>

<p>In a file named 6-job_creator.js:</p>

<li>Create a queue with Kue</li>
<li>Create an object containing the Job data with the following format:</li>
<pre>
{
  phoneNumber: string,
  message: string,
}
</pre>
<br>
<li>Create a queue named push_notification_code, and create a job with the object created before</li>
<li>When the job is created without error, log to the console Notification job created: JOB ID</li>
<li>When the job is completed, log to the console Notification job completed</li>
<li>When the job is failing, log to the console Notification job failed</li>
<pre>
bob@dylan:~$ npm run dev 6-job_creator.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
Notification job created: 1
</pre>

<p>Nothing else will happen - to process the job, go to the next task!</p>

<p>If you execute multiple time this file, you will see the JOB ID increasing - it means you are storing new job to process…</p>

<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 6-job_creator.js</li>
  
<b>7. Create the Job processor</b>
<p>In a file named 6-job_processor.js:</p>

<li>Create a queue with Kue</li>
<li>Create a function named sendNotification:
  <li>It will take two arguments phoneNumber and message</li>
  <li>It will log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE</li>
</li>
<li>Write the queue process that will listen to new jobs on push_notification_code:
  <li>Every new job should call the sendNotification function with the phone number and the message contained within the job data</li>
</li>
<b>Requirements:</b>

<li>You only need one Redis server to execute the program</li>
<li>You will need to have two node processes to run each script at the same time</li>
<li>You muse use Kue to set up the queue</li>
<b>Terminal 2:</b>
<pre>
bob@dylan:~$ npm run dev 6-job_processor.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_processor.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_processor.js`
Sending notification to 4153518780, with message: This is the code to verify your account
</pre><br>
<b>Terminal 1: let’s queue a new job!</b>
<pre>
bob@dylan:~$ npm run dev 6-job_creator.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "6-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 6-job_creator.js`
Notification job created: 2
</pre>

<b>And in the same time in Terminal 2:</b>
<pre>
Sending notification to 4153518780, with message: This is the code to verify your account
</pre>
<p>BOOM! same as 5-subscriber.js and 5-publisher.js but with a module to manage jobs.</p>

<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 6-job_processor.js</li>
  
<b>8. Track progress and errors with Kue: Create the Job creator</b>

<p>In a file named 7-job_creator.js:</p>

<p>Create an array jobs with the following data inside:</p>
<pre>
const jobs = [
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
</pre>
<p>After this array created:</p>

<li>Create a queue with Kue</p>
<li>Write a loop that will go through the array jobs and for each object:
  <li>Create a new job to the queue push_notification_code_2 with the current object</li>
  <li>If there is no error, log to the console Notification job created: JOB_ID</li>
  <li>On the job completion, log to the console Notification job JOB_ID completed</li>
  <li>On the job failure, log to the console Notification job JOB_ID failed: ERROR</li>
  <li>On the job progress, log to the console Notification job JOB_ID PERCENTAGE% complete</li>
</li>
<b>Terminal 1:</b>
<pre>
bob@dylan:~$ npm run dev 7-job_creator.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "7-job_creator.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 7-job_creator.js`
Notification job created: 39
Notification job created: 40
Notification job created: 41
Notification job created: 42
Notification job created: 43
Notification job created: 44
Notification job created: 45
Notification job created: 46
Notification job created: 47
Notification job created: 48
Notification job created: 49
</pre>
<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 7-job_creator.js</li>
  
<b>9. Track progress and errors with Kue: Create the Job processor</b>
<p>In a file named 7-job_processor.js:</p>

<p>Create an array that will contain the blacklisted phone numbers. Add in it 4153518780 and 4153518781 - these 2 numbers will be blacklisted by our jobs processor.
</p>
<p>Create a function sendNotification that takes 4 arguments: phoneNumber, message, job, and done:</p>

<li>When the function is called, track the progress of the job of 0 out of 100</li>
<li>If phoneNumber is included in the “blacklisted array”, fail the job with an Error object and the message: Phone number PHONE_NUMBER is blacklisted</li>
<li>Otherwise:
  <li>Track the progress to 50%</li>
  <li>Log to the console Sending notification to PHONE_NUMBER, with message: MESSAGE</li>
</li>
<p>Create a queue with Kue that will proceed job of the queue push_notification_code_2 with two jobs at a time.
</p>
<b>Requirements:</b>

<li>You only need one Redis server to execute the program</li>
<li>You will need to have two node processes to run each script at the same time</li>
<li>You muse use Kue to set up the queue</li>
<li>Executing the jobs list should log to the console the following:</li>

<b>Terminal 2:</b>
<pre>
bob@dylan:~$ npm run dev 7-job_processor.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "7-job_processor.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 7-job_processor.js`
Sending notification to 4153518743, with message: This is the code 4321 to verify your account
Sending notification to 4153538781, with message: This is the code 4562 to verify your account
Sending notification to 4153118782, with message: This is the code 4321 to verify your account
Sending notification to 4153718781, with message: This is the code 4562 to verify your account
Sending notification to 4159518782, with message: This is the code 4321 to verify your account
Sending notification to 4158718781, with message: This is the code 4562 to verify your account
Sending notification to 4153818782, with message: This is the code 4321 to verify your account
Sending notification to 4154318781, with message: This is the code 4562 to verify your account
Sending notification to 4151218782, with message: This is the code 4321 to verify your account
</pre><br>
<b>And in the same time in terminal 1:</b>
<pre>
...
Notification job #39 0% complete
Notification job #40 0% complete
Notification job #39 failed: Phone number 4153518780 is blacklisted
Notification job #40 failed: Phone number 4153518781 is blacklisted
Notification job #41 0% complete
Notification job #41 50% complete
Notification job #42 0% complete
Notification job #42 50% complete
Notification job #41 completed
Notification job #42 completed
Notification job #43 0% complete
Notification job #43 50% complete
Notification job #44 0% complete
Notification job #44 50% complete
Notification job #43 completed
Notification job #44 completed
Notification job #45 0% complete
Notification job #45 50% complete
Notification job #46 0% complete
Notification job #46 50% complete
Notification job #45 completed
Notification job #46 completed
Notification job #47 0% complete
Notification job #47 50% complete
Notification job #48 0% complete
Notification job #48 50% complete
Notification job #47 completed
Notification job #48 completed
Notification job #49 0% complete
Notification job #49 50% complete
Notification job #49 completed
</pre><br>
<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 7-job_processor.js</li>
  
<b>10. Writing the job creation function</b>
<p>In a file named 8-job.js, create a function named createPushNotificationsJobs:</p>

<li>It takes into argument jobs (array of objects), and queue (Kue queue)</li>
<li>If jobs is not an array, it should throw an Error with message: Jobs is not an array</li>
<li>For each job in jobs, create a job in the queue push_notification_code_3</li>
<li>When a job is created, it should log to the console Notification job created: JOB_ID</li>
<li>When a job is complete, it should log to the console Notification job JOB_ID completed</li>
<li>When a job is failed, it should log to the console Notification job JOB_ID failed: ERROR</li>
<li>When a job is making progress, it should log to the console Notification job JOB_ID PERCENT% complete</li>
<pre>
bob@dylan:~$ cat 8-job-main.js 
import kue from 'kue';

import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

const list = [
    {
        phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account'
    }
];
createPushNotificationsJobs(list, queue);

bob@dylan:~$
bob@dylan:~$ npm run dev 8-job-main.js 

> queuing_system_in_js@1.0.0 dev /root
> nodemon --exec babel-node --presets @babel/preset-env "8-job-main.js"

[nodemon] 2.0.4
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `babel-node --presets @babel/preset-env 8-job-main.js`
Notification job created: 51
</pre><br>

<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 8-job.js</li>
  
<b>11. Writing the test for job creation</b>
<p>Now that you created a job creator, let’s add tests:</p>

<li>Import the function createPushNotificationsJobs</li>
<li>Create a queue with Kue</li>
<li>Write a test suite for the createPushNotificationsJobs function:
  <li>Use queue.testMode to validate which jobs are inside the queue</li>
  <li>etc.</li>
</li>
<b>Requirements:</b>

<li>Make sure to enter the test mode without processing the jobs before executing the tests</li>
<li>Make sure to clear the queue and exit the test mode after executing the tests</li>
<pre>
bob@dylan:~$ npm test 8-job.test.js 

> queuing_system_in_js@1.0.0 test /root
> mocha --require @babel/register --exit "8-job.test.js"



  createPushNotificationsJobs
    ✓ display a error message if jobs is not an array
Notification job created: 1
Notification job created: 2
    ✓ create two new jobs to the queue
...

  123 passing (417ms)
</pre><br>
<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 8-job.test.js</li>
 
<b>12. In stock?</b>

<b>Data</b>
<p>Create an array listProducts containing the list of the following products:</p>

<li>Id: 1, name: Suitcase 250, price: 50, stock: 4</li>
<li>Id: 2, name: Suitcase 450, price: 100, stock: 10</li>
<li>Id: 3, name: Suitcase 650, price: 350, stock: 2</li>
<li>Id: 4, name: Suitcase 1050, price: 550, stock: 5</li>
<b>Data access</b>
<p>Create a function named getItemById:</p>

<li>It will take id as argument</li>
<li>It will return the item from listProducts with the same id</li>
<b>Server</b>
<p>Create an express server listening on the port 1245. (You will start it via: npm run dev 9-stock.js)</p>

<b>Products</b>
<p>Create the route GET /list_products that will return the list of every available product with the following <
JSON format:</p>
<pre>
bob@dylan:~$ curl localhost:1245/list_products ; echo ""
[{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4},{"itemId":2,"itemName":"Suitcase 450","price":100,"initialAvailableQuantity":10},{"itemId":3,"itemName":"Suitcase 650","price":350,"initialAvailableQuantity":2},{"itemId":4,"itemName":"Suitcase 1050","price":550,"initialAvailableQuantity":5}]
bob@dylan:~$ 
</pre>
<b>In stock in Redis</b>
<p>Create a client to connect to the Redis server:</p>

<li>Write a function reserveStockById that will take itemId and stock as arguments:
  <li>It will set in Redis the stock for the key item.ITEM_ID</li>
</li>
<li>Write an async function getCurrentReservedStockById, that will take itemId as an argument:
  <li>It will return the reserved stock for a specific item</li>
</li>
<b>Product detail</b>
<p>Create the route GET /list_products/:itemId, that will return the current product and the current available stock (by using getCurrentReservedStockById) with the following JSON format:</p>
<pre>
bob@dylan:~$ curl localhost:1245/list_products/1 ; echo ""
{"itemId":1,"itemName":"Suitcase 250","price":50,"initialAvailableQuantity":4,"currentQuantity":4}
bob@dylan:~$ 
</pre>
<p>If the item does not exist, it should return:</p>
<pre>
bob@dylan:~$ curl localhost:1245/list_products/12 ; echo ""
{"status":"Product not found"}
bob@dylan:~$ 
</pre>
<b>Reserve a product</b>
<p>Create the route GET /reserve_product/:itemId:</p>

  <li>If the item does not exist, it should return:</li>
  <pre>
bob@dylan:~$ curl localhost:1245/reserve_product/12 ; echo ""
{"status":"Product not found"}
bob@dylan:~$ 
</pre>
<li>If the item exists, it should check that there is at least one stock available. If not it should return:</li>
<pre>
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status":"Not enough stock available","itemId":1}
bob@dylan:~$ 
If there is enough stock available, it should reserve one item (by using reserveStockById), and return:
bob@dylan:~$ curl localhost:1245/reserve_product/1 ; echo ""
{"status":"Reservation confirmed","itemId":1}
bob@dylan:~$ 
</pre>
<b>Requirements:</b>

<li>Make sure to use promisify with Redis</li>
<li>Make sure to use the await/async keyword to get the value from Redis</li>
<li>Make sure the format returned by the web application is always JSON and not text</li>
<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 9-stock.js</li>
 
<b>13. Can I have a seat?</b>

<b>Redis</b>
<p>Create a Redic client:</p>

<li>Create a function reserveSeat, that will take into argument number, and set the key available_seats with the number</li>
<li>Create a function getCurrentAvailableSeats, it will return the current number of available seats (by using promisify for Redis)</li>
<li>When launching the application, set the number of available to 50</li>
<li>Initialize the boolean reservationEnabled to true - it will be turn to false when no seat will be available</li>
<b>Kue queue</b>
<p>Create a Kue queue</p>

<b>Server</b>
<p>Create an express server listening on the port 1245. (You will start it via: npm run dev 100-seat.js)</p>

<p>Add the route GET /available_seats that returns the number of seat available:</p>
<pre>
bob@dylan:~$ curl localhost:1245/available_seats ; echo ""
{"numberOfAvailableSeats":"50"}
bob@dylan:~$ 
</pre>
<p>Add the route GET /reserve_seat that:</p>

<li>Returns { "status": "Reservation are blocked" } if reservationEnabled is false</li>
<li>Creates and queues a job in the queue reserve_seat:
  <li>Save the job and return:
    <li>{ "status": "Reservation in process" } if no error</li>
    <li>Otherwise: { "status": "Reservation failed" }</li>
  </li>
  <li>When the job is completed, print in the console: Seat reservation job JOB_ID completed</li>
  <li>When the job failed, print in the console: Seat reservation job JOB_ID failed: ERROR_MESSAGE</li>
  <pre>
bob@dylan:~$ curl localhost:1245/reserve_seat ; echo ""
{"status":"Reservation in process"}
bob@dylan:~$ 
</pre>
<p>Add the route GET /process that:</p>

<li>Returns { "status": "Queue processing" } just after:</li>
<li>Process the queue reserve_seat (async):
  <li>Decrease the number of seat available by using getCurrentAvailableSeats and reserveSeat</li>
  <li>If the new number of available seats is equal to 0, set reservationEnabled to false</li>
  <li>If the new number of available seats is more or equal than 0, the job is successful</li>
  <li>Otherwise, fail the job with an Error with the message Not enough seats available</li>
  <pre>
bob@dylan:~$ curl localhost:1245/process ; echo ""
{"status":"Queue processing"}
bob@dylan:~$ 
bob@dylan:~$ curl localhost:1245/available_seats ; echo ""
{"numberOfAvailableSeats":"49"}
bob@dylan:~$ 
</pre>
<b>and in the server terminal:</b>

<pre>Seat reservation job 52 completed</pre>
<p>and you can reserve all seats:</p>
<pre>
bob@dylan:~$ for n in {1..50}; do curl localhost:1245/reserve_seat ; echo ""; done
{"status":"Reservation in process"}
{"status":"Reservation in process"}
...
{"status":"Reservation in process"}
{"status":"Reservation in process"}
{"status":"Reservation in process"}
{"status":"Reservation are blocked"}
{"status":"Reservation are blocked"}
{"status":"Reservation are blocked"}
bob@dylan:~$ 
</pre>
<b>Requirements:</b>

<li>Make sure to use promisify with Redis</li>
<li>Make sure to use the await/async keyword to get the value from Redis</li>
<li>Make sure the format returned by the web application is always JSON and not text</li>
<li>Make sure that only the allowed amount of seats can be reserved</li>
<li>Make sure that the main route is displaying the right number of seats</li>
<b>Repo:</b>

<li>GitHub repository: alx-backend</li>
<li>Directory: 0x03-queuing_system_in_js</li>
<li>File: 100-seat.js</li>

