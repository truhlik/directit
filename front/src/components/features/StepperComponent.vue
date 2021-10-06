<template>
    <div>
        <div class="form-con">
				<span class="title-tags">
					{{$t('projects.stepper.title')}}
				</span>
            <br>
            <small v-if="helpText">{{ helpText }}</small>
        </div>
        <div class="stepper-wrap">
            <div v-for="(value, index) in stepper"
                 :id="'step-' + value.num"
                 :key="index"
                 class="step-item"
                 v-bind:class="classObject(value.status)"
                 @click="stepClicked(index, value.status)">

                <span class="step-line"></span>
                <div class="step-num">
                    <span v-if="!value.active">{{ value.num }}</span>
                    <font-awesome-icon v-else icon="check"/>
                </div>
                <span class="step-name">
					{{ value.name }}
				</span>
                <b-popover :target="'step-' + value.num"
                           placement="top"
                           triggers="hover">
                    <!--					{{ value.help_text }}-->
                    <ProjectToolTips
                            :num="value.num" :services="sortedServices[value.num]"
                    />
                </b-popover>

            </div>
        </div>
        <div class="map-wrap">
            <span class="status-map"> <span class="circle not-demand"></span>Nepoptávám</span>
            <span class="status-map"> <span class="circle demand"></span>Poptávám</span>
            <span class="status-map"> <span class="circle in-progress"></span>Probíhá</span>
            <span class="status-map"> <span class="circle completed"></span>Hotovo</span>
        </div>
    </div>
</template>

<script>
    import {mapState, mapActions, mapMutations} from 'vuex'
    import ProjectToolTips from "~/components/features/include/ProjectToolTips";
    import {library} from '@fortawesome/fontawesome-svg-core'
    import {faCheck} from '@fortawesome/free-solid-svg-icons'

    library.add(faCheck);

    export default {
        name: 'stepper-component',
        components: {
            ProjectToolTips
        },
        props: {
            stepper: {},
            helpText: String
        },
        data: () => ({
            classObject: status => ({
                'not-demand': status === 0,
                'active demand': status === 10,
                'active in-progress': status === 20,
                'active completed': status === 30,
            }),
        }),
        methods: {
            stepClicked(stepIndex, status) {
                //console.log('stepClicked', stepIndex, status)
                status = status + 10;
                if (status > 30) status = 0

                const data = {
                    step: stepIndex + 1,
                    val: status
                };
                this.$emit('stepClick', data);
            },
            clickStepByServiceId(id) {
                //console.log('clickStepByServiceId(id)', id)
                if(!this.reverseServices) return;
                const step = this.reverseServices[id];
                //console.log({step})
                if(step) {
                    this.stepClicked(step, 10);
                }
            },
        },
        computed: {
            ...mapState({
                tags: state => state.tags.loadedTags,
                accessoriesTags: state => state.tags.accessoriesTags,
                allServices: state => state.services.all,
            }),
            sortedServices() {
                //console.log('this.allServices', this.allServices)
                if (!this.allServices) return;
                let result = {};
                this.allServices.results?.forEach(service => result[service.milestone] ? result[service.milestone].push(service) : result[service.milestone] = [service]);
                return result;
            },
            reverseServices() {
                if (!this.allServices) return;
                let result = {};
                this.allServices.results?.forEach(service => result[service.id] = this.stepper.findIndex(i => i.num == service.milestone));
                return result;
            },
        },
        created() {
            //this.id = this.$route?.query?.id
            (async () => {
                await this.$store.dispatch('services/getAll');
                const selectedServiceId = this.$route?.query['service-id'];
                if(selectedServiceId) this.clickStepByServiceId(selectedServiceId);
            })()
        },
    }
</script>

<style lang="scss" scoped>

    $xs-min: 576px;

    $ball-size: 40px;
    $item-width: 110px;
    $item-height: 80px;
    $bg-color: #fff;
    $text-size: 13px;

    $black: #000;
    $blue: #0984cc;
    $gray: #dee2e6;
    $green: #4fa570;
    $orange: #e65f1e;

    @media(min-width: 576px) {
        $ball-size: 60px;
        $item-width: 180px;
        $item-height: 130px;
        $bg-color: #fff;
        $text-size: 18px;
    }

    .stepper-wrap {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;

        .step-item {
            cursor: pointer;
            height: 96px;
            margin-bottom: 15px;
            position: relative;
            transition: all .5s;
            width: 120px;
            @media(min-width: $xs-min) {
                height: 100px;
                width: 131px;
            }

            &:hover {
                transform: scale(1.1);
                .step-num, .step-line {
                    color: #000;
                }

                &.demand {
                    .step-num, .step-line {
                        background-color: $blue;
                        border-color: $blue;
                        color: $white;
                    }
                    .step-name {
                        color: $black;
                    }
                }

                &.in-progress {
                    .step-num, .step-line {
                        background-color: $orange;
                        border-color: $orange;
                    }
                    .step-name {
                        color: $black;
                    }
                }

                &.completed {
                    .step-num, .step-line {
                        background-color: $green;
                        border-color: $green;
                    }
                    .step-name {
                        color: $green;
                    }
                }
            }

            &:last-child {
                .step-line {
                    width: 50%;
                }
            }
            &:first-child {
                .step-line {
                    left: 50%;
                    width: 50%;
                }
            }

            &.active {
                transform: scale(1.1);
                .step-num, .step-line {
                    color: #fff;
                }
            }

            &.demand {
                .step-num, .step-line {
                    background-color: $blue;
                    border-color: $blue;
                }
            }

            &.in-progress {
                .step-num, .step-line {
                    background-color: $orange;
                    border-color: $orange;
                }
            }

            &.completed {
                .step-num, .step-line {
                    background-color: $green;
                    border-color: $green;
                }
            }

        }

        .step-line {
            background-color: $gray;
            box-shadow: 6px 17px 46px -13px rgba(0, 0, 0, 0.75);
            display: block;
            height: 2px;
            left: 0;
            position: absolute;
            top: 50%;
            transform: translateY(-50%);
            transition: all .5s;
            width: 100%;
        }

        .step-num {
            align-items: center;
            background-color: $gray;
            border: 8px solid $bg-color;
            border-radius: 50%;
            display: flex;
            font-size: 0.88rem;
            height: 40px;
            justify-content: center;
            left: 50%;
            transform: translate(-50%, -50%);
            transition: all .5s;
            position: absolute;
            top: 50%;
            width: 40px;
            @media(min-width: $xs-min) {
                height: 50px;
                width: 50px;
            }
        }

        .step-name {
            background-color: $bg-color;
            display: block;
            font-size: 0.88rem;
            padding: 0 15px 0 10px;
            position: absolute;
            text-align: center;
            top: 100%;
            transform: translateY(-50%);
            width: 100%;
            @media(min-width: $xs-min) {
                font-size: 0.88rem;
            }

        }
    }

    .map-wrap {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        margin: 50px auto;
    }

    .status-map {
        display: flex;
        margin: 5px 10px;
    }

    .circle {
        border-radius: 50%;
        display: block;
        height: 20px;
        margin-right: 5px;
        width: 20px;

        &.not-demand {
            background-color: $gray;
        }

        &.demand {
            background-color: $blue;
        }

        &.in-progress {
            background-color: $orange;
        }

        &.completed {
            background-color: $green;
        }

    }
</style>
