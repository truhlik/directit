import Vue from 'vue';
import Vuex from 'vuex';

import { categories } from './categories'
import { companies } from './companies'
import { errors } from './errors'
import { files } from './files'
import { projects } from './projects'
import { software } from './software'
import { tags } from './tags'
import { user } from './user'
import { searchObject} from "./searchObject";
import { technologies} from "./technologies";

Vue.use(Vuex);

export const store = new Vuex.Store({
    modules: {
        categories,
        companies,
        errors,
        files,
        projects,
        software,
        tags,
        user,
        searchObject,
        technologies,
    }
});