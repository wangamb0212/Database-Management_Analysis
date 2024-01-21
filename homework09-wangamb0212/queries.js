// jobs queries

// 1.db.jobs.distinct('Career Level')
[
    'Entry-Level',
    'Executive',
    'Experienced (non-manager)',
    'Manager',
    'Student'
  ]
  


// 2.
db.jobs.find({'Posting Type':'External','Salary Frequency':'Hourly'},{'_id': 0, 'Agency':1,'Business Title':1, 'Salary Range To':1}).sort({'Salary Range To':-1}). limit(3)
[
  {
    Agency: 'DEPARTMENT OF CORRECTION',
    'Business Title': 'Staff Physician  (Part-Time)',
    'Salary Range To': 98.84
  },
  {
    Agency: 'FIRE DEPARTMENT',
    'Business Title': 'Telemetry Physician',
    'Salary Range To': 84.86
  },
  {
    Agency: 'DEPARTMENT OF CORRECTION',
    'Business Title': 'Staff Physician',
    'Salary Range To': 83.61
  }
]



// 3.
db.jobs.aggregate([{$match:{'Posting Type':'External','Full-Time/Part-Time indicator':'F'}},{$group:{_id:'$Agency',count:{$sum:1}}}]).sort({count:-1})
[
  { _id: 'DEPT OF ENVIRONMENT PROTECTION', count: 489 },
  { _id: 'HRA/DEPT OF SOCIAL SERVICES', count: 302 },
  { _id: 'DEPARTMENT OF TRANSPORTATION', count: 241 },
  { _id: 'DEPT OF HEALTH/MENTAL HYGIENE', count: 202 },
  { _id: 'NYC HOUSING AUTHORITY', count: 137 },
  { _id: 'DEPT OF DESIGN & CONSTRUCTION', count: 110 },
  { _id: 'HOUSING PRESERVATION & DVLPMNT', count: 104 },
  { _id: 'DEPT OF PARKS & RECREATION', count: 88 },
  { _id: 'OFFICE OF MANAGEMENT & BUDGET', count: 83 },
  { _id: 'LAW DEPARTMENT', count: 82 },
  { _id: 'DEPARTMENT OF CORRECTION', count: 79 },
  { _id: "ADMIN FOR CHILDREN'S SVCS", count: 73 },
  { _id: 'FIRE DEPARTMENT', count: 65 },
  { _id: 'BRONX DISTRICT ATTORNEY', count: 61 },
  { _id: 'OFFICE OF THE COMPTROLLER', count: 57 },
  { _id: 'FINANCIAL INFO SVCS AGENCY', count: 50 },
  { _id: 'TAXI & LIMOUSINE COMMISSION', count: 48 },
  { _id: 'DEPT OF CITYWIDE ADMIN SVCS', count: 45 },
  { _id: 'POLICE DEPARTMENT', count: 36 },
  { _id: 'DEPARTMENT OF CITY PLANNING', count: 32 }
]


// 4.
db.jobs.aggregate([
    {
      $match: {
        'Posting Type': 'External',
        'Full-Time/Part-Time indicator': 'F'
      }
    },
    {
      $group: {
        _id: '$Agency',
        count: { $sum: 1 }
      }
    },
    {
      $match: {
        'count': { $gte: 100 }
      }
    }
  ]).sort({ count: -1 })

  [
    { _id: 'DEPT OF ENVIRONMENT PROTECTION', count: 489 },
    { _id: 'HRA/DEPT OF SOCIAL SERVICES', count: 302 },
    { _id: 'DEPARTMENT OF TRANSPORTATION', count: 241 },
    { _id: 'DEPT OF HEALTH/MENTAL HYGIENE', count: 202 },
    { _id: 'NYC HOUSING AUTHORITY', count: 137 },
    { _id: 'DEPT OF DESIGN & CONSTRUCTION', count: 110 },
    { _id: 'HOUSING PRESERVATION & DVLPMNT', count: 104 }
  ]

// 5.
db.jobs.aggregate([
    {
      $match: {
        'Posting Type': 'External',
        'Full-Time/Part-Time indicator': 'F'
      }
    },
    {
      $group: {
        _id: '$Agency',
        count: { $sum: 1 }
      }
    },
    {
      $match: {
        'count': { $gte: 100 }
      }
    },
    {
      $project: {
        _id: 0,
        count: 1,
        agency: { $toLower: '$_id' }
      }
    }
  ]).sort({ count: -1 })
  
  [
    { count: 489, agency: 'dept of environment protection' },
    { count: 302, agency: 'hra/dept of social services' },
    { count: 241, agency: 'department of transportation' },
    { count: 202, agency: 'dept of health/mental hygiene' },
    { count: 137, agency: 'nyc housing authority' },
    { count: 110, agency: 'dept of design & construction' },
    { count: 104, agency: 'housing preservation & dvlpmnt' }
  ]


// 6.
db.jobs.aggregate([
  {
    $match: {
      'Salary Frequency': 'Annual'
    }
  },
  {
    $group: {
      _id: {
        $arrayElemAt: [
          { $split: ['$Posting Date', '/'] },
          2
        ]
      },
      average_salary: {
        $avg: '$Salary Range To'
      }
    }
  }
]).sort({
  _id: 1
})
[
    { _id: '2020', average_salary: 173486 },
    { _id: '2021', average_salary: 94162.5731707317 },
    { _id: '2022', average_salary: 96693.75169535734 },
    { _id: '2023', average_salary: 91866.24598959838 }
  ]
  