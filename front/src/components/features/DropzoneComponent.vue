<template>
  <div class="mb-5">
     <dropzone
             id="dropzone"
             :destroyDropzone="true"
             :options="options"
             ref="el"
             @vdropzone-success="onSuccessUpload"
     />
  </div>
</template>

<script>
  import Dropzone from 'nuxt-dropzone'
  import 'nuxt-dropzone/dropzone.css'

  export default {
    name: 'dropzone-component',
    components: {
      Dropzone
    },
    props: [
      'onSuccessEmit'
    ],
    data() {
      return {
        options: {
          dictDefaultMessage: this.$t('dropzone.zone_message'),
          headers: {
            "Authorization": window.localStorage.getItem('auth._token.local')
          },
          url: `${process.env.NUXT_ENV_API_URL}files/`,
        }
      }
    },
    mounted() {
      // Everything is mounted and you can access the dropzone instance
      const instance = this.$refs.el.dropzone
    },
    methods: {
      onSuccessUpload(file, response){
        this.$emit('onSuccessEmit', file, response);
      }
    }
  }
</script>

<style>

</style>
