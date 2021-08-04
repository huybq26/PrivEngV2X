const express = require('express');
const trajectoryRoutes = express.Router();
const Trajectory_raw = require('../../model/trajectory_raw');
const Trajectory_sanitized = require('../../model/trajectory_sanitized');
const config = require('config');
let fs = require('fs');

// let dataOut = '';
// const readTextFile = async (fileName) => {
//   let dataText = '';
//   let fs = require('fs');
//   await fs.readFile(fileName, 'utf8', (err, data) => {
//     console.log('OK: ' + fileName);
//     dataOut = data;
//     return data
//     // console.log(dataText);
//   });
//   return dataText;
// }

// Post the only data. We will replace this multiple times. No need to upload anymore.
// trajectoryRoutes.post('/', async (req, res) => {
//   try {
//     await fs.readFile('../x_y_bsm.txt', 'utf8', async (err, data) => {
//       // let raw_data = await readTextFile('../../x_y_bsm.txt');
//       const newTrajectory_raw = new Trajectory_raw({
//         name: 'only data',
//         data: data,
//       });
//       const trajectory_raw = await newTrajectory_raw.save();
//       res.json(trajectory_raw);
//       // console.log(dataText);
//     });
//     //   await fs.readFile('../../x_y_bsm_sanitized.txt', 'utf8', async (err, data) => {
//     //     // let raw_data = await readTextFile('../../x_y_bsm.txt');
//     //     const newTrajectory_sanitized = new Trajectory_sanitized({ data: data });
//     //     const trajectory_sanitized = await newTrajectory_sanitized.save();
//     //     res.json(trajectory_sanitized);
//     //     // console.log(dataText);
//     //   })
//   } catch (e) {
//     console.log(e);
//     res.status(500).send('Server Error');
//   }
// });

async function run() {
  let data = await fs.readFileSync('../x_y_bsm.txt', 'utf8');
  await Trajectory_raw.replaceOne(
    { name: 'only data' },
    { name: 'only data', data: data }
  );
  // console.log(data)
  // Trajectory_raw.insertOne(
  //   { name: 'only data' },
  //   { name: 'only data', data: data }
  // );
  // let newTrajectory_raw = new Trajectory_raw({
  //   name: 'only data',
  //   data: data,
  // });
  // await newTrajectory_raw.save();
  // console.log(data.toString());
  // res.json({ msg: data });
}
// for (i = 1; i <= 100; i++) {

// }
trajectoryRoutes.post('/replace', async (req, res) => {
  try {
    setInterval(() => {
      run();
      console.log('Hello!');
    }, 1000);
  } catch (error) {
    console.log(e);
  }
});

trajectoryRoutes.get('/getData', async (req, res) => {
  try {
    setInterval(async () => {
      let data = await Trajectory_raw.find({});
      console.log(data[0].data);
      fs.writeFileSync('../output.txt', data[0].data.toString());
    }, 1000);
  } catch (e) {
    console.log(e);
    res.status(500).send('Server Error');
  }
});

trajectoryRoutes.post('/new', async (req, res) => {
  try {
    let data = await fs.readFileSync('../hello.txt', 'utf8');
    const newTrajectory_raw = new Trajectory_raw({
      name: 'only data',
      data: data,
    });
    await newTrajectory_raw.save();
    res.json({ data });
  } catch (e) {
    console.log(e);
    res.status(500).send('Server Error');
  }
});

trajectoryRoutes.post('/', async (req, res) => {
  try {
    //   await fs.readFile('../../x_y_bsm_sanitized.txt', 'utf8', async (err, data) => {
    //     // let raw_data = await readTextFile('../../x_y_bsm.txt');
    //     const newTrajectory_sanitized = new Trajectory_sanitized({ data: data });
    //     const trajectory_sanitized = await newTrajectory_sanitized.save();
    //     res.json(trajectory_sanitized);
    //     // console.log(dataText);
    //   })
  } catch (e) {
    console.log(e);
    res.status(500).send('Server Error');
  }
});

trajectoryRoutes.get('/show', async (req, res) => {
  try {
    const data = await Trajectory_raw.find({});
    console.log(data.length);
    res.json({ msg: data });
  } catch (err) {
    console.error(err.message);
    res.status(500).send('Server Error');
  }
});

trajectoryRoutes.delete('/', async (req, res) => {
  try {
    // const post = await Trajectory_raw.find();
    const result = await Trajectory_raw.remove({}).exec();
    res.json({ msg: 'Post removed' });
  } catch (err) {
    console.error(err.message);

    res.status(500).send('Server Error');
  }
});

// trajectoryRoutes.get('/', async (req, res) => {
//     // const raw = database.collection("trajectory_raws");
//     // const sanitized = database.collection("trajectory_sanitizeds")
// function sleep(time) {
//   return new Promise((resolve) => setTimeout(resolve, time));
// }

// This code to send the data continuosly to the database
// for (let i = 0; i <= 10; i++) {
//   setTimeout(async function () {
//     await fs.readFile('../../x_y_bsm.txt', 'utf8', async (err, data) => {
//       // let raw_data = await readTextFile('../../x_y_bsm.txt');
//       const newTrajectory_raw = new Trajectory_raw({ data: data });
//       const trajectory_raw = await newTrajectory_raw.save();
//       res.json(trajectory_raw);
//       // console.log(dataText);
//     });
//   }, 5000);
// }
// for (i=0;i<=10;i++){
//     sleep(10000).then(() => {
//     fs.readFile('../../x_y_bsm.txt', 'utf8', async (err, data) => {
//     const newTrajectory_raw = new Trajectory_raw({ data: data });
//     const trajectory_raw = await newTrajectory_raw.save();
//     res.json(trajectory_raw);
//     // console.log(dataText);
//     })
// });

// var id = window.setInterval(function(){
//     if(i >= 10) {
//         clearInterval(id);
//         return;
//     }

//     console.log(i);
//     i++;
// }, 1000)

// })

let changeStream_raw;
let changeStream_sanitized;

changeStream_raw = Trajectory_raw.watch();
changeStream_sanitized = Trajectory_sanitized.watch();

changeStream_raw.on('change', (next) => {
  // process any change event
  console.log('received a change to the collection: \t');
});

module.exports = trajectoryRoutes;
