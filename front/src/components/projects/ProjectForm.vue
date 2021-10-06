<template>
    <div class="custom-container card pt-5">
        <b-tabs content-class="mt-3" justified pills fill align="center">
            <b-tab active>
                <template v-slot:title>
                    <font-awesome-icon class="ml-1"
                                       icon="project-diagram"
                    />&nbsp;
                    {{$t('projects.title')}}
                </template>
                <form class="mt-5">
                    <div class="form-con">
                        <b-row class="mb-3">
                            <b-col sm="6">
                                <b-form-group id="id_name_group"
                                              label-for="id_name"
                                              label-class="required"
                                              :label="$t('form.name')">
                                    <b-form-input id="id_name"
                                                  v-model="name"
                                                  :class="{ 'error' : objectError.name }"
                                                  required
                                                  :placeholder="$t('form.name')"
                                                  :disabled="disabledInputs"
                                                  @input="validate('name')">

                                    </b-form-input>
                                    <span class="text-danger" v-for="(error, index) in objectError.name" :key="index">{{ error }}<br></span>
                                </b-form-group>

                            </b-col>
                            <b-col sm="6">
                                <b-form-group label-for="id_due_date"
                                              :label="$t('form.due_date')">
                                    <date-picker id="id_due_date"
                                                 v-model="due_date"
                                                 :config="dueOptions"
                                                 :placeholder="$t('form.due_date')"
                                                 :disabled="disabledInputs"
                                    ></date-picker>

                                    <small v-if="helpText.due_date" class="help-text">{{ helpText.due_date }}</small>
                                </b-form-group>

                            </b-col>
                            <b-col sm="6">
                                <b-form-group label-for="id_status"
                                              :label="$t('form.status')">
                                    <b-form-select id="id_status"
                                                   v-model="status"
                                                   :options="statusTypes"
                                                   :disabled="disabledInputs"
                                    >

                                    </b-form-select>
                                </b-form-group>
                            </b-col>
                            <b-col v-if="update" sm="12">
                                <CategoriesComponent accessoriesType="categories"
                                                     :canAdd="isClient"
                                                     :modelWithCategories="project"
                                                     :propCategories="project && project.category_obj ? [project.category_obj] : null"
                                                     modelType="projects"
                                                     :senToApi="true"
                                                     :helpText="helpText.category"
                                                     :title="$t('form.categories')"/>
                            </b-col>
                            <b-col v-else sm="12">
                                <CategoriesComponent accessoriesType="categories"
                                                     :title="$t('form.categories')"
                                                     :modelWithCategories="project"
                                                     :helpText="helpText.category"
                                                     :required="true"/>
                            </b-col>
                            <b-col sm="12">
                                <b-form-group id="id_description_group"
                                              label-for="id_description"
                                              label-class="required"
                                              :label="$t('form.description')">
                                    <b-form-textarea id="id_description"
                                                     v-model="description"
                                                     :class="{ 'error' : objectError.description }"
                                                     :disabled="disabledInputs"
                                                     :placeholder="$t('form.description')"
                                                     @input="validate('description')">
                                    </b-form-textarea>
                                    <small v-if="helpText.description" class="help-text">{{ helpText.description }}</small>
                                    <span class="text-danger" v-for="(error, index) in objectError.description" :key="index">{{ error }}<br></span>
                                </b-form-group>
                            </b-col>
                            <b-col sm="12">
                                <FileComponent
                                        :canBeUpdated="!disabledInputs"
                                        :files="project.files"
                                        @getParentModel="getProjectDetail(project.id)"
                                />
                                <DropzoneComponent
                                        v-if="isClient"
                                        @onSuccessEmit="fileUploaded"
                                />
                            </b-col>
                        </b-row>
                    </div>
                    <b-row>
                        <b-col sm="12">
                            <StepperComponent :stepper="stepper"
                                              @stepClick="changeSteps"
                                              :helpText="helpText.stepper"
                            ></StepperComponent>
                        </b-col>
                        <b-col sm="12" class="d-flex justify-content-center mb-5 mt-2">
                            <b-button variant="primary"
                                      class="btn-transition btn-hover-shine custom-lg"
                                      :disabled="disabledInputs"
                                      @click="createUpdateProject">{{ update ? $t('form.button.save') : $t('form.button.create') }}
                            </b-button>
                        </b-col>
                        <b-col sm="12" md="6" class="mb-5 mt-5" v-if="project.consultant">
                            <div class="text-center">
                                <strong>Přidělený konzultant</strong>
                            </div>
                            <PersonCard
                                    v-if="project.consultant"
                                    :person="project.consultant"/>
                        </b-col>
                        <b-col sm="12" md="6" class="mb-5 mt-5" v-if="project.supplier">
                            <div class="text-center">
                                <strong>Přidělený dodavatel</strong>
                            </div>
                            <PersonCard
                                    v-if="project.supplier"
                                    :person="project.supplier"/>
                        </b-col>
                    </b-row>
                </form>
            </b-tab>
            <b-tab :disabled="!update">
                <template v-slot:title>
                    <font-awesome-icon class="ml-1"
                                       icon="comments"
                    /> &nbsp;
                    {{$t('projects.messages')}}&nbsp;
                    <span v-if="messagesCount">({{messagesCount}})</span>
                </template>
                <ProjectMessages :id="project.id"></ProjectMessages>
            </b-tab>
        </b-tabs>
    </div>
</template>

<script>
    import {mapActions, mapGetters, mapMutations, mapState} from 'vuex'
    import CategoriesComponent from "~/components/features/CategoriesComponent";
    import DropzoneComponent from "~/components/features/DropzoneComponent.vue";
    import FileComponent from "~/components/features/FileComponent.vue";
    import StepperComponent from "~/components/features/StepperComponent.vue";
    import {PROJECT_STATUS_TYPES} from "~/helpers/constants"
    import PersonCard from "~/components/company/PersonCard";
    import ProjectMessages from "./ProjectMessages";

    import {library} from '@fortawesome/fontawesome-svg-core'
    import {
        faProjectDiagram,
        faComments,
    } from '@fortawesome/free-solid-svg-icons'
    import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

    library.add(
        faProjectDiagram,
        faComments
    );

    export default {
        name: 'project-form',
        components: {
            ProjectMessages,
            CategoriesComponent,
            DropzoneComponent,
            PersonCard,
            StepperComponent,
            FileComponent
        },
        props: {
            update: Boolean,
        },
      created(){
        const nameFromQuery = this.$route?.query['service-name'];
        console.log({nameFromQuery})
        if(nameFromQuery) this.name = nameFromQuery;
      },
        data: () => ({
            dueOptions: {
                format: 'YYYY-MM-DD',
                locale: 'cs',
                icons: {
                    time: 'pe-7s-alarm big-icon',
                    date: 'pe-7s-date big-icon',
                    up: 'pe-7s-angle-up big-icon',
                    down: 'pe-7s-angle-down big-icon',
                    previous: 'pe-7s-angle-left big-icon',
                    next: 'pe-7s-angle-right big-icon',
                    close: 'pe-7s-close big-icon'
                }
            },
            helpText: {
                category: $nuxt.$t('help_text.project_category'),
                description: $nuxt.$t('help_text.project_description'),
                due_date: $nuxt.$t('help_text.project_due_date'),
                stepper: $nuxt.$t('help_text.project_stepper'),
            },
            objectValidator: {
                name: {
                    name: 'name',
                    rules: ['required']
                },
                description: {
                    name: 'description',
                    rules: ['required']
                },
            },
            statusTypes: PROJECT_STATUS_TYPES
        }),
        computed: {
            ...mapGetters({
                isClient: 'user/isClient',
            }),
            ...mapState({
                project: state => state.projects.project,
                selectCategories: state => state.categories.accessoriesCategories,
                objectError: state => state.errors.objectError,
                messagesCount: function (state) {
                    return state.projects.projectsMessages[this.project.id] ? state.projects.projectsMessages[this.project.id].root?.pagination.count : null
                },
            }),
            disabledInputs: function () {
                return !this.isClient
            },
            name: {
                get() {
                    return this.project.name || '';
                },
                set(name) {
                    return this.addToProject({name});
                }
            },
            due_date: {
                get() {
                    return this.project.due_date || '';
                },
                set(due_date) {
                    return this.addToProject({due_date});
                }
            },
            description: {
                get() {
                    return this.project.description || '';
                },
                set(description) {
                    return this.addToProject({description});
                }
            },
            status: {
                get() {
                    return this.project.status || 0;
                },
                set(status) {
                    return this.addToProject({status});
                }
            },
            stepper: {
                get() {
                    return [
                        /*{
                num: 1,
                name: 'Definice projektu',
                status: this.project.step1 || 0,
            },
            {
                num: 2,
                name: 'Základní návrh řešení',
                status: this.project.step2 || 0,
            },
            {
                num: 3,
                name: 'Studie trhu',
                status: this.project.step3 || 0,
            },
            {
                num: 4,
                name: 'Oslovení dodavatelů',
                status: this.project.step4 || 0,
            },
            {
                num: 5,
                name: 'Výběr dodavatele',
                status: this.project.step5 || 0,
            },
            {
                num: 6,
                name: 'Implementace',
                status: this.project.step6 || 0,
            }*/
                        {
                            num: 1,
                            name: 'Analýza',
                            status: this.project.step1 || 0,
                        },
                        {
                            num: 2,
                            name: 'Studie Trhu',
                            status: this.project.step2 || 0,
                        },
                        {
                            num: 3,
                            name: 'Selekce Dodavatelů',
                            status: this.project.step3 || 0,
                        },
                        {
                            num: 4,
                            name: 'Realizace',
                            status: this.project.step4 || 0,
                        },
                    ]
                }
            }
        },
        methods: {
            ...mapMutations('projects', {
                addToProject: 'addToProject'
            }),
            ...mapActions('projects', {
                createAPIProject: 'createProject',
                updateAPISoftware: 'updateProject',
                getProjectDetail: 'getProjectDetail'
            }),
            ...mapActions('categories', {
                getCategoriesId: 'getCategoriesId'
            }),
            ...mapActions('errors', {
                inputValidate: 'validate'
            }),
            getOptimalizedProject() {
                if (!this.project.hasOwnProperty('files')) return []
                let updated_project = {...this.project}
                updated_project.files = this.project.files.map(file => {
                    return file.id
                })
                return updated_project
            },
            changeSteps(data) {
                const key = 'step' + data.step;
                this.addToProject({[key]: data.val});
            },
            async createUpdateProject() {

                let categoriesID = await this.getCategoriesId(this.selectCategories);

                if (categoriesID.length === 0) {
                    categoriesID = await this.getCategoriesId(this.project.categories);
                }

                this.addToProject({categories: categoriesID});

                if (this.update) {
                    const optimalized_project = this.getOptimalizedProject()
                    this.updateAPISoftware(optimalized_project);
                } else {
                    this.createAPIProject(this.project);
                }
            },
            fileUploaded(file, response) {
                let files = []
                if (this.project.hasOwnProperty('files')) {
                    files = [...this.project.files]
                }

                if (this.update) {
                    files.push(response)
                    this.addToProject({files})

                    let updated_project = {...this.project}
                    delete updated_project.categories
                    updated_project.files = this.project.files.map(file => {
                        return file.id
                    })

                    this.updateAPISoftware(updated_project)
                } else {
                    files.push(response.id)
                    this.addToProject({files})
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
        }
    }
</script>

<style>
    .nav-link {
        font-size: 18px;
        text-align: center;
        display: block;
    }
</style>