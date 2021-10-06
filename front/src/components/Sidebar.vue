<template>
  <div
    :class="sidebarbg"
    class="app-sidebar sidebar-shadow"
    @mouseover="toggleSidebarHover('add', 'closed-sidebar-open')"
    @mouseleave="toggleSidebarHover('remove', 'closed-sidebar-open')"
  >
    <div class="app-header__logo">
      <nuxt-link to="/"
        ><img :src="logo" class="only-open big-logo"
      /></nuxt-link>
      <img :src="logoSmall" class="small-logo" />
    </div>
    <div class="app-sidebar-content">
      <VuePerfectScrollbar class="app-sidebar-scroll" v-once>
        <SidebarMenu
          :menu="getSideBarMenu"
          :showChild="true"
          @itemClick="onItemClick"
        />
      </VuePerfectScrollbar>
    </div>
    <!--<CallbackModal ref="childCallbackModal"
                   :modalName="modalName"
                   :infoText="modalInfoText"
                   :callbackType="callbackType"></CallbackModal>-->
    <AssistantModal
      ref="childAssistantModal"
      :modalName="modalName"
      :infoText="modalInfoText"
      :callbackType="assistantType"
    ></AssistantModal>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { SidebarMenu } from "vue-sidebar-menu";
import VuePerfectScrollbar from "vue-perfect-scrollbar";
//import CallbackModal from "~/components/user/modals/CallbackModal"
import AssistantModal from "~/components/user/modals/AssistantModal";

import logoSmall from "~/assets/images/logo/small_logo.svg";
import logo from "~/assets/images/logo/logo.svg";
import logoCut from "~/assets/images/logo/DirectiT4.svg";

export default {
  components: {
    SidebarMenu,
    VuePerfectScrollbar,
    //CallbackModal,
    AssistantModal,
  },
  data() {
    return {
      logo: logo,
      logoSmall: logoSmall,
      isOpen: false,
      sidebarActive: false,
      modalName: "",
      modalInfoText: "",
      callbackType: "",
      assistantType: "",
      collapsed: true,
      windowWidth: 0,
    };
  },
  props: {
    sidebarbg: String,
  },
  computed: {
    ...mapGetters({
      isClient: "user/isClient",
      isConsultant: "user/isConsultant",
      isSupplier: "user/isSupplier",
      hasFreePlan: "user/hasFreePlan",
      hasBasicPlan: "user/hasBasicPlan",
    }),
    getSideBarMenu() {
      const projectListMenu = {
        title: this.$t("menu.projects_list"),
        href: "/projekty/seznam/",
      };

        const refProjectsMenu = {
              title: this.$t('menu.reference_projects'),
              href: '/subjekty/referencni-projekty/',
        };

        const addRefProjectMenu = {
              title: this.$t('form.button.add_ref_project'),
              href: '/subjekt/referencni-projekt/',
        };

        const myRefProjectMenu = {
              title: this.$t('form.button.my_ref_projects'),
              href: '/subjekty/moje-referencni-projekty/',
        };

      // Položky v menu pro Dodavatele
      if (this.isSupplier) {
        let myItMenu = {
          icon: "pe-7s-note2",
          title: this.$t("menu.my_it"),
          child: [
              projectListMenu,
              refProjectsMenu,
              addRefProjectMenu,
              myRefProjectMenu,
          ],
        };
        return [myItMenu];
      }

      // Položky v menu pro Konzultanty
      if (this.isConsultant) {
        let myItMenu = {
          icon: "pe-7s-note2",
          title: this.$t("menu.my_it"),
          child: [
              projectListMenu,
              refProjectsMenu,
              addRefProjectMenu,
              myRefProjectMenu,
          ],
        };
        return [myItMenu];
      }

      // Položky v menu pro Klienty
      if (this.isClient) {
        return this.getClientMenuItems();
      }
    },
  },
  methods: {
    toggleBodyClass(className) {
      const el = document.body;
      this.isOpen = !this.isOpen;

      if (this.isOpen) {
        el.classList.add(className);
      } else {
        el.classList.remove(className);
      }
    },
    toggleSidebarHover(add, className) {
      const el = document.body;
      this.sidebarActive = !this.sidebarActive;

      this.windowWidth = document.documentElement.clientWidth;

      if (this.windowWidth > "992") {
        if (add === "add") {
          el.classList.add(className);
        } else {
          el.classList.remove(className);
        }
      }
    },
    getWindowWidth(event) {
      const el = document.body;

      this.windowWidth = document.documentElement.clientWidth;

      if (this.windowWidth < "1350") {
        el.classList.add("closed-sidebar", "closed-sidebar-md");
      } else {
        el.classList.remove("closed-sidebar", "closed-sidebar-md");
      }
    },
    onItemClick(event, item) {
      if (item && item.hasOwnProperty("modal")) {
        this.modalName = item.title;
        this.modalInfoTe = item.infoText;
        //this.callbackType = item.type;
        this.assistantType = item.type;
        this.$refs[item.modal].openModal();
      }
    },
    getClientMenuItems() {
      const logoImg = {
        data() {
          return {
            src: logoCut,
          };
        },
        template: '<img :src="src">',
      };

      let myItMenu = {
        icon: "pe-7s-note2",
        title: this.$t("menu.my_it"),
        child: [
          {
            title: this.$t("menu.add_software"),
            href: "/technologie/vytvorit/",
          },
          {
            title: this.$t("menu.software_list"),
            href: "/technologie/seznam/",
          },
          {
            title: this.$t("menu.project_create"),
            href: "/projekty/vytvorit/",
          },
          {
            title: this.$t("menu.projects_list"),
            href: "/projekty/seznam/",
          },
        ],
      };

      let dbMenu = {
        icon: "pe-7s-search",
        title: this.$t("menu.database"),
        child: [
          {
            title: this.$t("menu.search_suppliers"),
            href: "/subjekty/seznam-dodavatelu/",
          },
        ],
      };

      let servicesMenu = {
        icon: "pe-7s-tools",
        title: this.$t("menu.services"),
        class: "sidebar-logo",
        //image: "logo/DirectiT4.svg",
        child: [
          /*{
              title: this.$t('menu.analysis'),
              href: '/sluzby/strategicka-analyza/'
            },
            {
              title: this.$t('menu.it_consierge'),
              modal: "childCallbackModal",
              type: "consierge",
              infoText: this.$t('services.it_consierge.info_text')
            },
            {
              title: this.$t('menu.callback'),
              modal: "childCallbackModal",
              type: "callback",
              infoText: this.$t('services.callback.info_text')
            },*/
          {
            title: this.$t("menu.analyzes_studies"),
            href: "/sluzby/analyzy-a-studie/",
          },
          {
            title: this.$t("menu.ict_services"),
            href: "/sluzby/ict-sluzby/",
          },
          {
            title: this.$t("menu.consultants_specialists"),
            href: "/sluzby/konzultanti-a-specialiste/",
          },
          {
            title: this.$t("menu.it_assistant"),
            modal: "childAssistantModal",
            type: "it_assistant",
            infoText: this.$t("services.it_assistant.info_text"),
            disabled: this.hasFreePlan || this.hasBasicPlan,
          },
        ],
      };

      let menu = [myItMenu, dbMenu];

      dbMenu.child.push({
        title: this.$t("menu.search_consultants"),
        href: "/subjekty/seznam-konzultantu/",
        disabled: this.hasFreePlan,
      });
      menu.push(servicesMenu);

        dbMenu.child.push(
            {
                title: this.$t('menu.search_technologies'),
                href: '/subjekty/seznam-technologii/',
            },
        )

        dbMenu.child.push(
            {
                title: this.$t('menu.reference_projects'),
                href: '/subjekty/referencni-projekty/',
            },
        )

      return menu;
    },
  },
  mounted() {
    this.$nextTick(function () {
      window.addEventListener("resize", this.getWindowWidth);
      //Init
      this.getWindowWidth();
    });
  },
  beforeDestroy() {
    window.removeEventListener("resize", this.getWindowWidth);
  },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Yellowtail&display=swap");

.only-closed,
.only-open {
  transition: all 0.5s ease-in-out;
}

.closed-sidebar:nisclientot(.closed-sidebar-open) {
  .app-header__logo img {
    margin-left: -5px;
    width: 250px;
  }
}

.closed-sidebar-open:not(.closed-sidebar) {
  .app-header__logo img {
    width: 180px;
  }
}

.app-header__logo img {
  margin-right: 10px;
  width: 180px;
}
</style>
