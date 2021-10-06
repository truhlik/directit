<template>
    <div>
        <b-modal ref="order-modal"
                 class="order-modal"
                 hide-footer
                 centered
                 @hide="modalHided">
            <template v-slot:modal-title>
                {{$t('company.requests.title')}}
            </template>
            <div class="text-center mb-4">
                <img class="order-logo"
                     :src="company.image"
                     v-if="!orderSent && company">
                <i v-if="orderSent"
                   class="pe-7s-check check-icon"></i>
                <span v-if="orderSent" class="info">
                    {{$t('company.requests.sent')}}
                </span>

                <h2 class="text-center mt-3 text-break"
                    v-if="company">{{ company.name }}</h2>
            </div>
            <form v-if="!orderSent">
                <b-row>
                    <b-col sm="12" v-if="isConsultant">
                        <b-form-group id="order-date-from-group"
                                      label-for="id-date-from"
                                      :label="$t('form.date_from')">
                            <date-picker id="id_date_from"
                                         v-model="order.date_from"
                                         :config="fromOptions"
                                         :placeholder="$t('form.date_from')"></date-picker>
                        </b-form-group>

                    </b-col>
                    <b-col sm="6" v-if="isConsultant">
                        <b-form-group id="order-duration-length"
                                      label-for="id_duration_length"
                                      :label="$t('form.duration_length')">
                            <b-form-input id="id_duration_length"
                                          v-model="order.duration_length"
                                          type="number"
                                          :placeholder="$t('form.duration_length')"></b-form-input>
                        </b-form-group>

                    </b-col>
                    <b-col sm="6" class="d-flex align-items-end" v-if="!isSupplier">
                        <b-form-group id="order-duration-unit">
                            <b-form-select id="id_duration_unit"
                                           v-model="order.duration_unit"
                                           :options="durationOptions"></b-form-select>
                        </b-form-group>

                    </b-col>
                    <b-col sm="12"
                           class="mt-2"
                           v-if="!company">
                        <i>Poptávám konzultanta s těmito znalostmi:</i>
                        <CategoriesComponent accessoriesType="categories"
                                             :title="$t('form.categories')"
                                             :modelWithCategories="order"
                        ></CategoriesComponent>
                    </b-col>
                    <b-col sm="12"
                           v-if="!company">
                        <!--<TagsComponent accessoriesType="tags"
                                                            :title="$t('form.tags')"
                                                            :modelWithCategories="order"
                                                            ></TagsComponent>-->
                        <ProductsComponent accessoriesType="products"
                                           :title="$t('form.products')"
                                           :modelWithCategories="order"
                        ></ProductsComponent>
                    </b-col>
                    <b-col sm="12">
                        <b-form-group v-if="" id="order-note-group"
                                      label-for="id-order-note"
                                      :label="
                                      isConsultant ? $t('form.note_write_consultant') : (isSupplier ? $t('form.note_write_supplier') : null)
">
                            <b-form-textarea :placeholder="$t('form.note')"
                                             id="id-order-note"
                                             v-model="order.note">
                            </b-form-textarea>
                        </b-form-group>
                    </b-col>
                    <b-col sm="12" class="d-flex justify-content-center">
                        <b-button class="mt-2 mr-2 btn-transition btn-hover-shine custom-md"
                                  variant="primary"
                                  @click="sendOrder"
                                  :disabled="sending">
                            <b-spinner variant="primary" v-if="sending"></b-spinner>
                            {{ $t('form.button.order') }}
                        </b-button>
                    </b-col>
                </b-row>
            </form>
            <div v-else class="text-center">
                <b-row>
                    <b-col sm="12"
                           v-if="order.note">
                        <span><strong>Poznámka: </strong>{{ order.note }}</span>
                    </b-col>
                    <b-col sm="12"
                           v-if="order.date_from">
                        <span><strong>Datum od: </strong>{{ order.date_from }}</span>
                    </b-col>
                    <b-col sm="12"
                           v-if="order.duration_length">
                        <span><strong>Trvání: </strong>{{ order.duration_length }} {{ unitOptions[order.duration_unit] }}</span>
                    </b-col>
                    <b-col>
                        <b-button class="mr-2 mb-2 mt-4 btn-transition"
                                  variant="outline-danger"
                                  size="lg"
                                  @click="deleteOrder()">
                            <font-awesome-icon class="mr-2" icon="trash-alt"/>
                            Spletl jsem se. {{ $t('form.button.takeback') }}
                        </b-button>
                    </b-col>
                    <b-col>
                        <b-button class="mr-2 mb-2 mt-4 btn-hover-shine btn-transition"
                                  variant="primary"
                                  size="lg"
                                  @click="hideModal">
                            <font-awesome-icon class="mr-2" icon="check"/>
                            Vše v pořádku. {{ $t('form.button.close') }}
                        </b-button>
                    </b-col>
                </b-row>
            </div>
        </b-modal>
    </div>
</template>

<script>
    import CategoriesComponent from "~/components/features/CategoriesComponent";
    import TagsComponent from "~/components/features/TagsComponent";
    import ProductsComponent from "~/components/features/ProductsComponent";
    import {mapActions, mapState} from 'vuex'
    import {library} from '@fortawesome/fontawesome-svg-core'
    import {faTrashAlt, faCheck} from '@fortawesome/free-solid-svg-icons'

    library.add(faTrashAlt, faCheck);

    export default {
        name: 'order-modal',
        components: {
            CategoriesComponent,
            TagsComponent,
            ProductsComponent,
        },
        props: ['company', 'type'],
        data: () => ({
            url: 'orders/',
            orderSent: false,
            order: {
                duration_unit: 'HOURS',
                duration_length: 1
            },
            fromOptions: {
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
            unitOptions: {
                'HOURS': 'Hodin',
                'DAY': 'Dní',
                'MONTH': 'Měsíců'
            },
            durationOptions: [
                {value: 'HOURS', text: 'Hodin'},
                {value: 'DAY', text: 'Dní'},
                {value: 'MONTH', text: 'Měsíců'},
            ],
            sending: false,
        }),
        computed: {
            ...mapState({
                orderTags: state => state.tags.accessoriesTags,
                orderProducts: state => state.products.accessoriesProducts,
                orderCategories: state => state.categories.accessoriesCategories
            }),
            isSupplier() {
                return this.company?.role == 'SUPPLIER' || this.type == 'SUPPLIER';
            },
            isConsultant() {
                return this.company?.role == 'CONSULTANT' || this.type == 'CONSULTANT';
            },
        },
        methods: {
            ...mapActions('categories', {
                getCategoriesId: 'getCategoriesId'
            }),
            ...mapActions('tags', {
                getTagsId: 'getTagsId'
            }),
            ...mapActions('products', {
                getProductsId: 'getProductsId'
            }),
            showModal() {
                this.$refs['order-modal'].show();
            },
            hideModal() {
                this.$refs['order-modal'].hide();
            },
            async setTagsCategories() {
                if (this.orderCategories?.length) {
                    this.order['categories'] = await this.getCategoriesId(this.orderCategories);
                }
                if (this.orderTags?.length) {
                    this.order['tags'] = await this.getTagsId(this.orderTags);
                }
                if (this.orderProducts?.length) {
                    this.order['products'] = await this.getProductsId(this.orderProducts);
                }
            },
            async sendOrder() {
                this.sending = true
                if (this.company) {
                    this.order.company = this.company.id;
                } else {
                    await this.setTagsCategories();
                }
                const response = this.$axios.$post(this.url, this.order)
                this.$toast.success(this.$t('form.actions.sent'));
                this.orderSent = true;
                this.order = response;
                this.sending = false
            },
            async deleteOrder() {
                const url = this.url + this.order.id + '/';
                await this.$axios.$delete(url).then(
                    response => {
                        this.$toast.success(this.$t('form.actions.deleted'));
                        this.hideModal();
                    }
                )
            },
            modalHided() {
                this.order = {
                    duration_unit: 'HOURS',
                    duration_length: 1
                };
                this.orderSent = false;
            }
        }
    }
</script>