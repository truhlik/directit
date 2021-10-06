<template>
    <div class="custom-container card pt-5">
        <!-- <pre>{{project}}</pre> -->
        <form class="mt-5">
            <div class="form-con">
                <b-row class="mb-3 solver" v-if="update && project.solver_obj && isClient">
                    <b-col sm="12">
                        <company-widget :company="project.solver_obj"></company-widget>
                    </b-col>
                </b-row>
                <b-row class="mb-3">
                    <b-col sm="6">
                        <b-form-group id="id_title_group"
                                      label-for="id_title"
                                      label-class="required"
                                      :label="$t('form.title')">
                            <b-form-input id="id_title"
                                          v-model="title"
                                          :class="{ 'error' : objectError.title }"
                                          required
                                          :placeholder="$t('form.title')"
                                          @input="validate('title')">

                            </b-form-input>
                            <span class="text-danger" v-for="(error, index) in objectError.title" :key="index">{{
                                    error
                                }}<br></span>
                        </b-form-group>
                    </b-col>
                    <!-- <b-col sm="6">
                        <b-form-group id="id_contact_name_group"
                                      label-for="id_contact_name"
                                      label-class="required"
                                      :label="$t('form.contact_name')">
                            <b-form-input id="id_contact_name"
                                          v-model="contact_name"
                                          :class="{ 'error' : objectError.contact_name }"
                                          required
                                          :placeholder="$t('form.contact_name')"
                                          @input="validate('contact_name')">

                            </b-form-input>
                            <span class="text-danger" v-for="(error, index) in objectError.contact_name"
                                  :key="index">{{ error }}<br></span>
                        </b-form-group>
                    </b-col>
                    <b-col sm="6">
                        <b-form-group id="id_contact_email_group"
                                      label-for="id_contact_email"
                                      label-class="required"
                                      :label="$t('form.contact_email')">
                            <b-form-input id="id_contact_email"
                                          v-model="contact_email"
                                          :class="{ 'error' : objectError.contact_email }"
                                          required
                                          :placeholder="$t('form.contact_email')"
                                          @input="validate('contact_email')">

                            </b-form-input>
                            <span class="text-danger" v-for="(error, index) in objectError.contact_email" :key="index">{{
                                    error
                                }}<br></span>
                        </b-form-group>
                    </b-col> -->
                    <b-col sm="6">
                        <b-form-group id="id_sector_group"
                                      label-for="id_sector"
                                      label-class="required"
                                      :label="$t('form.sector')">
                            <b-form-select id="id_sector"
                                           v-model="sector"
                                           :options="sectorOptions"
                                           :class="{ 'error' : objectError.sector }"
                                           required
                                           :placeholder="$t('form.sector')"
                                           @input="validate('sector')"></b-form-select>
                            <span class="text-danger" v-for="(error, index) in objectError.sector" :key="index">{{
                                    error
                                }}<br></span>
                        </b-form-group>
                    </b-col>
                    <b-col sm="12">
                        <CategoriesComponent accessoriesType="categories"
                                             :title="$t('form.categories')"
                                             :propCategories="project && project.category_obj ? [project.category_obj] : null"
                                             modelType="references"
                                             :modelWithCategories="project"
                                             :helpText="helpText.category"
                                             :required="false"
                                             :singleOnly="true"
                                             :senToApi="update"/>
                    </b-col>
                    <b-col sm="12">
                        <ProductsComponent accessoriesType="products"
                                           :title="$t('form.products')"
                                           :modelWithProducts="project"
                                           :helpText="helpText.products"
                                           :required="false"
                                           :propProducts="project.products_obj"/>
                    </b-col>
                    <b-col sm="6">
                        <b-form-group id="id_problem_text_group"
                                      label-for="id_problem_text"
                                      label-class=""
                                      :label="$t('form.problem_text')">
                            <b-form-textarea id="id_problem_text"
                                             v-model="problem_text"
                                             :class="{ 'error' : objectError.problem_text }">

                            </b-form-textarea>
                            <span class="text-danger" v-for="(error, index) in objectError.problem_text"
                                  :key="index">{{ error }}<br></span>
                        </b-form-group>
                    </b-col>
                    <b-col sm="6">
                        <b-form-group id="id_solution_text_group"
                                      label-for="id_solution_text"
                                      label-class=""
                                      :label="$t('form.solution_text')">
                            <b-form-textarea id="id_solution_text"
                                             v-model="solution_text"
                                             :class="{ 'error' : objectError.solution_text }">

                            </b-form-textarea>
                            <span class="text-danger" v-for="(error, index) in objectError.solution_text" :key="index">{{
                                    error
                                }}<br></span>
                        </b-form-group>
                    </b-col>
                    <b-col sm="12">
                        <b-form-group id="id_benefits_text_group"
                                      label-for="id_benefits_text"
                                      label-class=""
                                      :label="$t('form.benefits_text')">
                            <b-form-textarea id="id_benefits_text"
                                             v-model="benefits_text"
                                             :class="{ 'error' : objectError.benefits_text }">

                            </b-form-textarea>
                            <span class="text-danger" v-for="(error, index) in objectError.benefits_text" :key="index">{{
                                    error
                                }}<br></span>
                        </b-form-group>
                    </b-col>
                    <b-col sm="12">
                        <FileComponent
                            :files="project.files_obj"
                            @getParentModel="getRefProjectDetail(project.id)"
                        />
                        <DropzoneComponent
                            @onSuccessEmit="fileUploaded"
                        />
                    </b-col>

                </b-row>
            </div>
            <b-row>
                <b-col sm="12" class="d-flex justify-content-center mb-5 mt-2">
                    <b-button variant="primary"
                              class="btn-transition btn-hover-shine custom-lg"
                              @click="createUpdateProject">{{
                            update ? $t('form.button.save') : $t('form.button.create')
                        }}
                    </b-button>
                </b-col>
            </b-row>
        </form>
    </div>
</template>

<script>
import {mapActions, mapGetters, mapMutations, mapState} from 'vuex'
import CategoriesComponent from "~/components/features/CategoriesComponent";
import ProductsComponent from "~/components/features/ProductsComponent";
import FileComponent from "../features/FileComponent";
import DropzoneComponent from "../features/DropzoneComponent";
import CompanyWidget from "../company/CompanyWidget";

export const SECTOR_OPTIONS = [
    {value: 1, text: "Bankovnictví, Finanční služby"},
    {value: 2, text: "Energetika"},
    {value: 3, text: "Informační technologie"},
    {value: 4, text: "Kultura"},
    {value: 5, text: "Lesnictví, těžba"},
    {value: 6, text: "Logistika, Transport"},
    {value: 7, text: "Média"},
    {value: 8, text: "Retail, Obchod"},
    {value: 9, text: "Služby"},
    {value: 10, text: "Stavebnictví"},
    {value: 11, text: "Telekomunikace"},
    {value: 12, text: "Turistický ruch, Pohostinství"},
    {value: 13, text: "Veřejný sektor"},
    {value: 14, text: "Výrobní průmysl"},
    {value: 15, text: "Vzdělávání"},
    {value: 16, text: "Zábavní průmysl"},
    {value: 17, text: "Zdravotnictví, Farmaceutický Průmysl"},
    {value: 18, text: "Zemědělství, Potravinářství"},
    {value: 19, text: "Ostatní"},
];

export default {
    name: "ProjectForm",
    components: {
        CompanyWidget,
        DropzoneComponent,
        FileComponent,
        CategoriesComponent,
        ProductsComponent,
    },
    props: {
        update: Boolean,
    },
    created() {
        if (!this.update) this.clearRefProject()
        this.title = this.$route?.query?.title || this.title
        const category = this.$route?.query?.category
        //console.log('route category', category)
        if (category) this.setAccessoriesCategory(JSON.parse(category));
    },
    data: () => ({
        helpText: {
            category: $nuxt.$t('help_text.project_category_single'),
            products: $nuxt.$t('help_text.project_products'),
            description: $nuxt.$t('help_text.project_description'),
            due_date: $nuxt.$t('help_text.project_due_date'),
            stepper: $nuxt.$t('help_text.project_stepper'),
        },
        objectValidator: {
            title: {
                name: 'title',
                rules: ['required']
            },
            contact_name: {
                name: 'contact_name',
                rules: ['required']
            },
            contact_email: {
                name: 'contact_email',
                rules: ['required']
            },
            sector: {
                name: 'sector',
                rules: ['required']
            },
        },
        sectorOptions: SECTOR_OPTIONS,
    }),
    computed: {
        ...mapState({
            objectError: state => state.errors.objectError,
            selectCategories: state => state.categories.accessoriesCategories,
            selectProducts: state => state.products.accessoriesProducts,
            project: state => state.projects.refProject,
        }),
        ...mapGetters({
            isClient: 'user/isClient',
            isSupplier: 'user/isSupplier',
            isConsultant: 'user/isConsultant',
        }),
        title: {
            get() {
                return this.project.title || '';
            },
            set(title) {
                return this.addToProject({title});
            }
        },
        contact_name: {
            get() {
                return this.project.contact_name || '';
            },
            set(contact_name) {
                return this.addToProject({contact_name});
            }
        },
        contact_email: {
            get() {
                return this.project.contact_email || '';
            },
            set(contact_email) {
                return this.addToProject({contact_email});
            }
        },
        sector: {
            get() {
                return this.project.sector || '';
            },
            set(sector) {
                return this.addToProject({sector});
            }
        },
        problem_text: {
            get() {
                return this.project.problem_text || '';
            },
            set(problem_text) {
                return this.addToProject({problem_text});
            }
        },
        solution_text: {
            get() {
                return this.project.solution_text || '';
            },
            set(solution_text) {
                return this.addToProject({solution_text});
            }
        },
        benefits_text: {
            get() {
                return this.project.benefits_text || '';
            },
            set(benefits_text) {
                return this.addToProject({benefits_text});
            }
        },
    },
    methods: {
        ...mapActions('categories', {
            getCategoriesId: 'getCategoriesId',
            getRefProjectDetail: 'getRefProjectDetail',
        }),
        ...mapActions('products', {
            getProductsId: 'getProductsId'
        }),
        ...mapMutations('projects', {
            addToProject: 'addToRefProject', clearRefProject: 'clearRefProject',
        }),
        ...mapMutations('categories', {
            setAccessoriesCategory: 'setAccessoriesCategory',
        }),
        ...mapActions('projects', {
            createAPIProject: 'createRefProject',
            updateAPISoftware: 'updateRefProject',
            getProjectDetail: 'getRefProjectDetail'
        }),
        ...mapActions('errors', {
            inputValidate: 'validate'
        }),
        mapFilesObj(files){
            return files.map(file => {
                return file.id
            }).filter(n => n)
        },
        getOptimalizedProject() {
            if (!this.project.hasOwnProperty('files')) return []
            let updated_project = {...this.project}
            updated_project.files = this.mapFilesObj(this.project.files)
            console.log('files', updated_project.files, this.project.files);
            return updated_project
        },
        async createUpdateProject() {

            const categoriesIds = await this.getCategoriesId(this.selectCategories);

            let categoryID;
            if (categoriesIds.length) {
                categoryID = categoriesIds[0];
            } else {
                categoryID = await this.getCategoriesId(this.project.categories)[0];
            }
            //console.log({categoryID, categoriesIds})
            let productsID = await this.getProductsId(this.selectProducts);

            if (productsID.length === 0) {
                productsID = await this.getProductsId(this.project.products);
            }

            this.addToProject({category: categoryID});
            this.addToProject({products: productsID});

            if (this.update) {
                // const optimalized_project = this.getOptimalizedProject()
                // this.updateAPISoftware(optimalized_project);
                this.updateAPISoftware(this.project);
            } else {
                this.createAPIProject(this.project);
            }
        },
        validate(input) {
            const data = {
                name: input,
                objectData: this.project,
                objectValidator: this.objectValidator
            };
            this.inputValidate(data);
        },
        fileUploaded(file, response) {
            let files = []
            if (this.project.hasOwnProperty('files')) {
                files = [...this.project.files]
            }

            if (this.update) {
                files.push(response.id)
                this.addToProject({files})

                let updated_project = {...this.project}
                delete updated_project.categories
                updated_project.files =  files
                this.updateAPISoftware(updated_project)
                this.project = updated_project;
            } else {
                files.push(response.id)
                this.addToProject({files})
            }

        },
    },
}
</script>

<style scoped lang="scss">
.solver {
    margin: auto;
    max-width: 500px;
}
</style>