<template>
    <div class="app-page-title">
        <div class="page-title-wrapper">
            <div class="page-title-heading">
                <div class="page-title-icon">
                    <i :class="icon" v-if="!image"/>
                    <b-img v-bind="mainProps" rounded alt="Rounded image" v-if="image" src="image"></b-img>
                </div>
                <div>
                    {{heading}}
                    <div class="page-title-subheading">
                        {{subheading}}
                    </div>
                </div>
            </div>
            <div v-if="delButton"
                 class="page-title-actions">
                <DelButton :model="model"
                           :modelName="modelName"></DelButton>
            </div>
            <div v-if="pathUrl || pathLink"
                 class="page-title-actions">
                <nuxt-link class="btn-shadow d-inline-flex align-items-center btn btn-primary"
                           :to="pathLink ? localePath({name: pathLink, params: {}}) : { path: pathUrl }">
                    <font-awesome-icon class="mr-2" :icon="pathIcon"/>
                    {{ pathName }}
                </nuxt-link>
            </div>

            <div v-if="orderButton"
                 class="page-title-actions">
                <b-button class="btn-shadow d-inline-flex align-items-center btn"
                          variant="primary"
                          @click="openOrderModal">
                    <font-awesome-icon class="mr-2" icon="user-tie"/>
                    <span v-if="type=='CONSULTANT'">{{$t('company.requests.consultant')}}</span>
                    <span v-if="type=='SUPPLIER'">{{$t('company.requests.supplier')}}</span>
                </b-button>
                <OrderModal ref="childOrderModal" :type="type"></OrderModal>
            </div>

            <div v-if="profillButton"
                 class="page-title-actions">
                <nuxt-link class="btn-shadow d-inline-flex align-items-center btn btn-primary"
                           :to="localePath({name: `subjekty-type-id`, params: { id: model.id, type: companyUrls[model.role] }})">
                    <font-awesome-icon class="mr-2" icon="user-tie"/>
                    Profil {{ model.name }}
                </nuxt-link>
                <OrderModal ref="childOrderModal"></OrderModal>
            </div>

        </div>
    </div>
</template>

<script>
    import {library} from '@fortawesome/fontawesome-svg-core'
    import {faPlus, faFileExcel, faUserTie, faList} from '@fortawesome/free-solid-svg-icons'
    import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
    import DelButton from '~/components/features/DelButton';

    import OrderModal from "~/components/orders/OrderModal";
    import {COMPANY_URLS} from "~/helpers/constants";

    library.add(
        faPlus, faFileExcel, faUserTie, faList
    );

  export default {
    components: {
      'font-awesome-icon': FontAwesomeIcon,
	    'DelButton': DelButton,
	    OrderModal: OrderModal
    },
    props: {
	    delButton: Boolean,
      heading: String,
      icon: String,
	    listUrl: Boolean,
	    model: Object,
	    modelName: String,
	    nameUrl: String,
	    orderButton: Boolean,
	    pathIcon: String,
	    pathName: String,
	    pathUrl: String,
        pathLink: String,
	    profillButton: Boolean,
      subheading: String,
        image: String,
        type: String,
    },
	  data: () => ({
		  companyUrls: COMPANY_URLS,
          mainProps: null
	  }),
	  methods: {
      openOrderModal() {
        this.$refs['childOrderModal'].showModal();
      }
	  }
  }
</script>
