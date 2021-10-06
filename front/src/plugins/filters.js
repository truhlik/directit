import Vue from 'vue'

export function getFileExtensionIcon(data){
  let icon = 'file' // set default icon
  if(!data?.length) return icon

  let extension = data.toLowerCase().substr(data.length - 8).split('.')[1]

  const iconTypesObject = {
    'file-pdf': ['pdf'],
    'file-csv': ['csv'],
    'file-excel': ['xls', 'xlsx'],
    'file-image': ['jpg', 'jpeg', 'png', 'svg'],
    'file-powerpoint': ['ppt','pptx'],
    'file-video': ['mp4', 'wave', 'webm', 'wmv', 'mov', 'ogg', 'mpg', 'mpeg'],
    'file-word': ['doc', 'docx']
  }
  for(let iconType in iconTypesObject){
    //   console.log(iconTypes[i])
    if( iconTypesObject[iconType].includes(extension)){
      icon = iconType
      break;
    }
  }
  return icon
}

export function getFileTitle(file){
  if(!file?.length) return 'Neznámý soubor'
  const pieces = file.toLowerCase().split('/')
  return pieces[pieces.length - 1]
}

export function trimText(value, length) {
  if(!value) return '';
  return value.substring(0, length) + (value.length > length ? '...' : '');
}

Vue.filter('get-file-icon', getFileExtensionIcon)
Vue.filter('get-file-name', getFileTitle)
Vue.filter('trimText', trimText)
