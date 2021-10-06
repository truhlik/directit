export default function ({ store }) {
  store.dispatch('errors/cleanErrorObject');
  //store.dispatch('companies/clearAllCompanyState');
  store.dispatch('tags/clearTagStates');
  store.dispatch('categories/clearCategoriesState');
  store.dispatch('projects/clearProjects');
}