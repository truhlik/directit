<template>
  <div>
    <b-modal ref="deleteObjectModal"
             id="deleteObjectModal"
             hide-footer
             centered>
      <template v-slot:modal-title>
        <h4 class="text-center">Smazat <strong v-if="title">{{ title }}</strong> <strong v-else-if="deletingModel.file">{{ deletingModel.file | get-file-name }}</strong>?</h4>
      </template>

      <div class="w-100 d-flex justify-content-center">
        <b-button
                variant="danger"
                size="lg"
                @click="deleteObject()"
        >
          Smazat
        </b-button>
        <b-button
                class="ml-5"
                variant="success"
                size="lg"
                @click="closeModal"
        >
          Ne, ponechat
        </b-button>
      </div>
    </b-modal>
  </div>
</template>

<script>
  export default {
    name: 'delete-modal',
    props: {
      title: {
        type: String,
        default: ''
      },
      deleteFunction: {
        type: Function
      },
      deletingModel: {
        type: Object,
        default: {}
      }
    },
    methods: {
      deleteObject(){
        console.log('deletgin modal before')
        this.$emit('deleteFunction', this.deletingModel)
      },
      closeModal(){
        this.$refs['deleteObjectModal'].hide();
      },
      openModal(){
        this.$refs['deleteObjectModal'].show();
      }
    }
  }
</script>