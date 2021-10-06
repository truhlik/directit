export default function ({ store, route, redirect }) {
  if(store.getters['user/isClient'] && !store.getters['user/hasFreePlan']){
    return
  }

  // Povolené URL pro všechny typy obchodních subjektů
  let allowedUrlsName = ['uzivatel-upravit___cs','subjekt-id-upravit___cs', 'subjekt-vytvorit___cs', 'login___cs',
    'index___cs', 'subjekt-referencni-projekt___cs']

  // Povolené URL pro Klienta, který má FREE plan
  if(store.getters['user/isClient'] && store.getters['user/hasFreePlan']){
    allowedUrlsName.push('subjekty-seznam-dodavatelu___cs',  'subjekty-seznam-technologii___cs', 'subjekty-referencni-projekty___cs', 'projekty-seznam___cs', 'projekty-vytvorit___cs',
      'projekty-id-upravit___cs', 'technologie-id-upravit___cs', 'technologie-vytvorit___cs', 'technologie-seznam___cs', 'sluzby-analyzy-a-studie___cs', 'sluzby-ict-sluzby___cs', 'sluzby-konzultanti-a-specialiste___cs')
    if(route.params?.type === 'suppliers') {
      allowedUrlsName.push('subjekty-type-id___cs')
    }
  }

  // Povolené URL pro Konzultanty
  if(store.getters['user/isConsultant']){
    allowedUrlsName.push('projekty-seznam___cs', 'projekty-id-upravit___cs', 
        'subjekty-referencni-projekty___cs', 'referencni-projekty-id-upravit___cs', 'referencni-projekty-id-detail___cs', 'subjekty-moje-referencni-projekty___cs')
  }

  // Povolené URL pro Dodavatele
  if(store.getters['user/isSupplier']){
    allowedUrlsName.push('projekty-seznam___cs', 'projekty-id-upravit___cs',
        'subjekty-referencni-projekty___cs', 'referencni-projekty-id-upravit___cs', 'referencni-projekty-id-detail___cs', 'subjekty-moje-referencni-projekty___cs')
  }

  if( allowedUrlsName.includes(route.name) ){
    return
  }

  return redirect('/')
}