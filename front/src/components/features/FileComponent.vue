<template>
    <div class="files-wrapper">
        <div class="label d-flex justify-content-start justify-content-md-between">
      <span>
        Soubory
      </span>
            <span>
          <b-alert
                  :value="true"
                  variant="info"
                  icon="info"
                  outline
          >
                  <font-awesome-icon class="mr-1" icon="info-circle"/>
          {{$t('files.limit')}}
        </b-alert>
      </span>
        </div>
        <div class="file-wrap"
             :key="file.id"
             v-for="(file, index) in files"
        >
            <div class="file-icons">
                <b-link
                        :href="file.file"
                        target="_blank"
                >
                    <font-awesome-icon class="ml-1" :icon="file.file | get-file-icon "/>
                </b-link>
                <font-awesome-icon class="ml-1 update-icon"
                                   v-if="canBeUpdated"
                                   @click="openFileModal(file)"
                                   icon="pencil-alt"
                />
                <font-awesome-icon class="ml-1 delete-icon"
                                   v-if="canBeUpdated"
                                   @click="openDeleteModal(file)"
                                   icon="times"
                />
            </div>
            <div class="file-info">
                <strong v-if="file.title">{{ file.title }}</strong>
                <strong v-else>{{ file.file | get-file-name }}</strong><br>
                {{ file.description }}
            </div>
        </div>
        <span v-if="files.length === 0"
              class="mb-3"
        >Nejsou uloženy žádné soubory.</span>


        <FileModalComponent
                ref="file-modal-component"
                @updateFunction="handlerUpdateFile"
        />
        <DeleteModal
                ref="delete-modal"
                @deleteFunction="handleDeleteFile"
                :deletingModel="file"
                :title="(file.title ? file.title : null )"
        />
    </div>
</template>

<script>
    import DeleteModal from "~/components/features/DeleteModal";
    import FileModalComponent from "~/components/files/FileModalComponent";
    import {mapActions, mapMutations, mapState} from 'vuex'

    import {library} from '@fortawesome/fontawesome-svg-core'
    import {
        faFile,
        faFileCsv,
        faFileExcel,
        faFileImage,
        faFilePdf,
        faFilePowerpoint,
        faFileVideo,
        faFileWord,
        faPencilAlt,
        faTimes,
        faInfoCircle
    } from '@fortawesome/free-solid-svg-icons'
    import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'

    library.add(
        faFile, faFileCsv, faFileExcel, faFileImage, faFilePdf, faFilePowerpoint, faFileVideo, faFileWord, faPencilAlt, faTimes, faInfoCircle
    );

    export default {
        name: 'file-component',
        components: {
            'font-awesome-icon': FontAwesomeIcon,
            'FileModalComponent': FileModalComponent,
            'DeleteModal': DeleteModal
        },
        props: {
            files: {
                type: Array,
                default: function () {
                  return []
                }
            },
            getParentModel: {
                type: Function
            },
            canBeUpdated: {
                type: Boolean,
                default: true
            }
        },
        computed: {
            ...mapState({
                file: state => state.files.file
            }),
        },
        methods: {
            ...mapActions({
                deleteFile: 'files/deleteFile',
                updateFile: 'files/updateFile'
            }),
            ...mapMutations({
                setFile: 'files/setFile'
            }),
            handleDeleteFile(file) {
                this.deleteFile(file)
                this.$refs['delete-modal'].closeModal()
                this.$emit('getParentModel')
            },
            handlerUpdateFile(file) {
                const data = {...file}
                this.updateFile(data)
                this.$refs['file-modal-component'].closeModal()
                this.$emit('getParentModel')
            },
            openFileModal(file) {
                this.setFile(file)
                this.$refs['file-modal-component'].openModal()
            },
            openDeleteModal(file) {
                this.setFile(file)
                this.$refs['delete-modal'].openModal()
            }
        }
    }
</script>