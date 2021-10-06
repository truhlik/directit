// LICENCE TYPES
export const LICENCE_TYPE = {
  '': 'Vyberte...',
  'PERPETUAL': 'Doživotní',
  'SUBSCRIPTION': 'Pronájem'
};

// LICENCE METRICS
export const LICENCE_METRIC = {
  '': 'Vyberte...',
  'USER': 'Počet uživatelů',
  'DEVICE': 'Počet zařízení',
  'HW': 'Počet jader / RAM',
  'OTHER': 'JIné',
};

// CALLBACK TYPES
export const CALLBACK_TYPE = {
  'SURVEY': 'Průzkum trhu',
  'REFERENCE': 'Nezávislá reference',
  'CONSULTATION': 'Konzultace k vybranému projektu',
  'EXPERTIZE': 'Expertní názor',
  'OTHER': 'Ostatní'
};

// Assistant TYPES
export const ASSISTANT_TYPE = {
    'SURVEY': 'Průzkum trhu',
    'REFERENCE': 'Nezávislá reference',
    'CONSULTATION': 'Konzultace k vybranému projektu',
    'EXPERTIZE': 'Expertní názor',
    'OTHER': 'Ostatní'
};

/* URLS CONSTANTS */
export const COMPANY_URLS = {
  'CONSULTANT': 'consultants',
  'SUPPLIER': 'suppliers'
};

// PROJECT STEPS
const PROJECT_STEP_NOT_DEMAND = 0;
const PROJECT_STEP_DEMAND = 10
const PROJECT_STEP_IN_PROGRESS = 20
const PROJECT_STEP_COMPLETED = 30

export const PROJECT_STEPS_TYPES = {
  PROJECT_STEP_NOT_DEMAND: 0,
  PROJECT_STEP_DEMAND: 10,
  PROJECT_STEP_IN_PROGRESS: 20,
  PROJECT_STEP_COMPLETED: 30,
};

// PROJECT STATUS TYPES
const PROJECT_STATUS_NEW = 0
const PROJECT_STATUS_HOLD = 10
const PROJECT_STATUS_IN_PROGRESS = 20
const PROJECT_STATUS_COMPLETED = 30

export const PROJECT_STATUS_TYPES = {
  [PROJECT_STATUS_NEW]: 'Nový',
  [PROJECT_STATUS_HOLD]: 'Pozastavený',
  [PROJECT_STATUS_IN_PROGRESS]: 'Probíhá',
  [PROJECT_STATUS_COMPLETED]: 'Hotový',
}

