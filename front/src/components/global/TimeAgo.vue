<template>
    <span>
        {{$t('datetime.before.title')}}
        {{previousTimeSinceObject.number}}
        {{$t('datetime.before.' + previousTimeSinceObject.type + '.' + (previousTimeSinceObject.number == 1 ? 'singular' : 'plural'))}}
     </span>
</template>

<script>
    import {timeSince} from '~/helpers/datetime'

    export default {
        name: "TimeAgo",
        props: {
            previousDate: Date | String,
            currentDate: Date | String,
        },
        computed: {
            convertedPreviousDate:
                function () {
                    return this.previousDate instanceof Date ? this.previousDate : new Date(this.previousDate)
                },
            convertedCurrentDate: function () {
                return this.currentDate ? (this.currentDate instanceof Date ? this.currentDate : new Date(this.currentDate)) : null
            },
            previousTimeSinceObject: function () {
                return timeSince(this.convertedPreviousDate, this.convertedCurrentDate)
            },
        }
    }
</script>

<style scoped>

</style>