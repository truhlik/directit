<template>
    <div class="app-page-disclaimer mb-4">
        {{text}}
    </div>
</template>

<script>
export default {
    name: "PageDisclaimer",
    props: {
        text: String,
    }
}
</script>

<style scoped lang="scss">
    .app-page-disclaimer {
        color: $gray;
    }
</style>