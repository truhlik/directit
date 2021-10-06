export default (context) => {
    return new Promise(function (resolve) {
        resolve({
            account: {
                account_credentials: 'Vaše uživatelské údaje',
                user_credentials: 'Uživatelské údaje',
                personal_credentials: 'Osobní údaje',
                your_profile: 'Váš profil',
                your_public_profile: 'Váš veřejný profil',
                account_company_administrator: 'Administrátor firemního účtu',
                account_administrator: 'Administrátor účtu',
                add_new_password: 'Zadejte Vaše nové heslo',
                change_your_password: 'Změňte si Vaše heslo',
                email: 'Váš email',
                first_name: 'Jméno',
                forgot_password: 'Zapomenuté heslo',
                last_name: 'Příjmení',
                login: 'Přihlásit se',
                logging_in: 'Přihlašování',
                logging_failed: 'Přihlásení se nepovedlo.',
                logged_in: 'Přihlášení proběhlo úspěšně',
                new_password_saved: 'Nové heslo bylo úspěšně uloženo. Nyní se můžete přihlásit.',
                password: 'Heslo',
                password_again: 'Heslo znovu',
                password_changed: 'Heslo bylo úspěšně změněno.',
                registration: 'Registrace',
                registration_client: 'Registrace pro klienty',
                registration_client_infotext: 'Registrací získáváte bezplatný přístup do konzultační platformy Direct IT a všem příslušným zdrojům pro Vaše projekty. Přístup zahrnuje přehled dodavatelů, technologií a dalších informací z ICT trhu.',
                registration_consultant: 'Registrace pro konzultanty',
                registration_supplier: 'Registrace pro dodavatele',
                sign_in: 'Zaregistrovat se',
                your_email: 'Zadejte Váš email',
                welcome: 'Vítejte zpět, prosím, přihlašte se.',
                completation_tips_title_consultant: 'Několik tipů pro kompletaci Vašeho profilu:',
                completation_tips_title_supplier: 'Několik tipů pro kompletaci Vašeho firemního profilu:',
                completation_tips: {
                    tip1: 'Přejděte do sekce Firemní profil v pravém horním rohu',
                    tip2: 'Nahrajte Firemní Logo',
                    tip3: 'Zkontrolujte všechny kontaktní údaje a to, zda jsou to ty, kam chcete aby Vás zákazníci kontaktovali',
                    tip4: 'Doplňte si Tagy: technologie, kterým se věnujete a máte příslušně kompetence',
                    tip5: 'Doplňte si Kategorie: Obory a řešení, kterým se věnujete a máte příslušně kompetence',
                    tip6: 'Přidejte popis Vaši společnosti, to nejdůležitější pro Vaše stávající i potenciální klienty',
                    tip7: 'Přidejte stručný popis Vašich zkušeností a zaměření.',
                    tip8: 'Vložte jakýkoli referenční projekt, na kterém jste pracoval/a a který chcete prozentovat potenciálním klientům.',

                },
            },
            form: {
                address: 'Adresa',
                cancel: 'Zrušit',
                date_from: 'Datum od',
                duration_length: 'Odhadovaná doba trvání',
                email_sent: 'E-mail byl odeslán, prosím, zkontrolujte Vaši e-mailovou schránku',
                ico: 'IČO',
                callback_type: 'Typ požadavku',
                assistant_type: 'Typ požadavku',
                categories: 'Kategorie',
                products: 'Produkty / Technologie',
                sector: 'Sektor',
                city: 'Město',
                company_name: 'Název firmy',
                due_date: 'Plánované dokončení',
                job: 'Pracovní pozice',
                street: 'Ulice',
                street_number: 'Číslo popisné',
                zip: 'PSČ',
                dic: 'DIČ',
                name: 'Název',
                contact_name: 'Kontaktní jméno',
                first_name: 'Jméno',
                licence_count: 'Počet Licencí / Zařízení',
                licence_type: 'Typ licence',
                licence_unit: 'Metrika',
                service_contact: 'Servisní kontakt',
                last_name: 'Příjmení',
                need_customization: 'Potřeba customizace',
                need_extension: 'Potřeba rozšíření',
                need_upgrade: 'Potřeba aktualizace / nahrazení',
                description: 'Popis',
                password: 'Heslo',
                phone: 'Telefon',
                status: 'Stav projektu',
                email: 'E-mail',
                contact_email: 'kontaktní e-mail',
                website: 'Webové stránky',
                search_in_input: 'Vyhledat podle názvu, tagu, kategorie ...',
                note: 'Poznámka',
                note_write_supplier: 'Napište zprávu dodavateli',
                note_write_consultant: 'Napište zprávu konzultantovi',
                reg_number: 'IČO',
                tags: 'Tagy',
                time: 'Čas',
                title: 'Titulek',
                user_count: 'Počet uživatelů',
                username: 'Uživatelské jméno',
                full_name: 'Vaše jméno',
                licence_till: 'Aktualizace do',
                find_alternative: 'Zajímá mě alternativa',
                your_first_name: 'Vaše jméno',
                your_phone: 'Váš telefon',
                watch_expiration: 'Sledovat expiraci',
                message_placeholder: 'Vložte text příspěvku',
                problem_text: 'Zadání / problém',
                solution_text: 'Řešení',
                benefits_text: 'Přínosy',
                logo_company: 'Logo firmy',
                profile_image: 'Profilová fotografie',
                button: {
                    change: 'Změnit',
                    create: 'Vytvořit',
                    detail: 'Detail',
                    details: 'Detaily',
                    takeback: 'Vzít zpět',
                    search: 'Hledat',
                    save: 'Uložit',
                    update: 'Upravit',
                    close: 'Zavřít',
                    send: 'Odeslat',
                    logout: 'Odhlásit',
                    delete: 'Smazat',
                    password_change: 'Změna hesla',
                    order: 'Objednat',
                    request: 'Poptat',
                    profile: 'Profil',
                    profile_edit: 'Úprava profilu',
                    reply: 'Odpovědět',
                    submit: 'Odeslat',
                    show_replies: 'Zobrazit odpovědi',
                    hide_replies: 'Skrýt odpovědi',
                    add_as_ref_project: 'Přidat jako referenční projekt',
                    add_ref_project: 'Přidat referenční projekt',
                    my_ref_projects: 'Moje referenční projekty',
                },
                actions: {
                    added: 'Přidáno',
                    created: 'Úspěšně vytvořeno',
                    deleted: 'Smazáno',
                    updated: 'Upraveno',
                    loaded: 'Načteno',
                    sent: 'Úspěšně odesláno. Děkujeme.',
                    saved: 'Úspěšně uloženo'
                }
            },
            company: {
                roles: {
                    consultant: 'Konzultant',
                    supplier: 'Dodavatel',
                    client: 'Klient',
                },
                requests: {
                    title: 'Poptávka',
                    sent: 'Poptávka byla úspěšně odeslána.',
                    consultant: 'Poptávám konzultanta',
                    supplier: 'Poptávám dodavatele',
                },
                buttons: {
                    fill_company_detail: 'Předvyplnit údaje podle IČO',
                },
                list: 'Seznam',
                loadMore: 'Načíst další',
                update: 'Úprava firmy',
                detail: 'Základní informace'
            },
            technology: {
                found: 'Nalezeno',
                found_categories: 'kategorií',
                found_subcategories: 'sekcí',
                found_products: 'produktů',
                subcategories_count: 'sekcí',
                loading_product: 'Načítání produktu...',
                vendor: 'Vendor',
                applied_technologies: 'Využité technologie',
            },
            callback: {
                types: {
                    survey: 'Expert Callback',
                    reference: 'Reference',
                    other: 'Ostatní'
                },
                messages: {
                    error: 'Forumulář se nepovedlo odeslat'
                }
            },
            messages: {
                company: {
                    created: 'Společnost byla vytvořena.'
                },
                callback: {
                    sent: 'Úspěšně odesláno'
                }
            },
            searcher: 'Vyhledávač',
            menu: {
                add_software: 'Zadat technologii',
                administration: 'Administrace',
                analysis: 'Strategická analýza',
                callback: 'Expert Callback',
                company: 'Firmy',
                createCompany: 'Vytvoření firmy',
                database: 'Subjekty & Technologie',
                it_consierge: 'IT Consierge',
                it_assistant: 'IT Assistant',
                list_consultants: 'Seznam konzultantů',
                listCompany: 'Seznam firem',
                list_suppliers: 'Seznam dodavatelů',
                myCompanies: 'Můj seznam firem',
                my_it: 'Moje IT',
                profile: 'Profil',
                project_create: 'Vytvořit projekt',
                ref_project_create: 'Vytvořit referenční projekt',
                ref_project_detail: 'Detail referenčního projektu',
                projects_list: 'Moje projekty',
                search: 'Vyhledávání',
                search_suppliers: 'Seznam dodavatelů',
                search_consultants: 'Seznam konzultantů',
                search_technologies: 'Katalog',
                reference_projects: 'Referenční projekty',
                my_reference_projects: 'Moje referenční projekty',
                services: 'Služby',
                software: 'Technologie',
                software_list: 'Moje technologie',
                user_profile: 'Uživatelský účet',
                company_profile: 'Firemní účet',
                consultant_profile: 'Účet konzultanta',
                analyzes_studies: 'Analýzy & Studie',
                ict_services: 'ICT Služby',
                consultants_specialists: 'Konzultanti a specialisté',
            },
            testimonial: {
                title: {
                    title: 'Reference',
                    evaluate: 'Přidat hodnocení',
                    eval_text: 'Vaše hodnocení'
                },
                button: {
                    add: 'Přidat referenci'
                }
            },
            software: {
                title: 'Technologie',
                create_title: 'Evidence technologie',
                update_title: 'Úprava technologie'
            },
            projects: {
                title: 'Projekt',
                title_plural: 'Projekty',
                title_create: 'Vytvořit projekt',
                title_update: 'Úprava projektu',
                messages: 'Zprávy',
                stepper: {
                    title: 'Mám zájem o:',
                },
            },
            services: {
                it_assistant: {
                    title: 'IT Asistent',
                    info_text: '',
                },
                monitored_technologies: {
                    title: 'Sledované technologie',
                },
                it_consierge: {
                    info_text: 'Zadejte jednoduché úkoly spojené s vaším IT jako je průzkum trhu, přehled dostupných řešení či IT adiministrativou Vašemu nezávislému asistentovi.',
                },
                callback: {
                    info_text: 'V případě potřeby konzultace k danému tématu či rychlého odborného názoru na věc stačí vybrat vhodný termín a čas a nezávislý expert z teamu Direct IT se Vám následně ozve.'
                },
                analysis: {
                    info_text: 'Vyberte si některý z 18 nejčastěji analyzovaných okruhů pro optimalizaci Vašeho IT. Pro každý okruh provedeme high-level analýzu v rámci Vašeho základního členství a navrhneme další postup.'
                },
                analyzes_studies: {
                    info_text: 'Získáváme maximum informací z trhu pro výběr těch nejlepších řešení za nejlepších podmínek.'
                },
                ict_services: {
                    info_text: 'Flexibilní ICT Služby přímo v rámci platfromy Direct IT'
                },
                consultants_specialists: {
                    info_text: 'Poskytujeme IT Experty pro jednorázovou i dlouhodobou spolupráci jak pro tvorbu nových IT projektů, tak údržbu stávajících systémů a řešení.'
                },
            },
            help_text: {
                project_category: 'Pro urychlení alokace zdrojů a zařazení projektu můžete přidat související kategorie',
                project_category_single: 'Pro urychlení alokace zdrojů a zařazení projektu můžete vybrat související kategorii',
                project_products: 'Přidejte produkty',
                project_description: 'Doplňte prosím krátký komentář k jednotlivým milníkům v rámci kterých chcete spolupracovat. Případně doplníme vše za vás po osobní konzultaci.',
                project_due_date: 'Zadejte prosím termín očekávaného dokončení',
                project_stepper: 'Zde máte možnost využít nezávislou expertizu pro každý krok projektového cyklu. Vyberte prosím, v jakých fázích chcete spolupracovat či potřebujete asistenci',
                software_category: 'Pro urychlení alokace zdrojů a zařazení technologie můžete přidat související kategorie',
                suppliers_list: 'V rámci seznamu dodavatelů lze podle zadaných parametrů vyhledávat a lokalizovat příslušné firmy. Vybrané společnosti za Vás můžeme kontaktovat pro spolupráci na projektech, poskytnutí indikativních nabídek, reference, expertní názor a další informace.',
                consultants_list: 'V rámci seznamu konzultantů lze podle zadaných parametrů vyhledávat a lokalizovat příslušné IT profesionály. Vybrané konzultanty za Vás můžeme kontaktovat pro spolupráci na projektech, poskytnutí indikativních nabídek, reference, expertní názor a další informace.',
                technologies_list: 'Katalog Direct IT přináší ucelený přehled výrobců, produktů a technologií napříč všemi hlavními sekcemi a s konkrétními vazbami na český ICT trh.',
                reference_project: 'Zde můžete přidat vybrané referenční projekty, na kterých jste pracovali a které chcete prezentovat potenciálním klientům. Zvýšíte tak svoji viditelnost v rámci platformy a potenciál pro nové příležitosti.',
                reference_projects: 'V přehledu referenčních projektů naleznete ukázky využití konkrétních produktů a technologií při řešení reálných ICT projektů z praxe.'
            },
            project_stepper: {
                title: 'Mám zájem o:',
                step1: 'Definice problémů a cílů které budou řešením projektu adresovány. Pohled IT a businessu. Přehled vztahů a zainteresovaných stran a proveditelnost.',
                step2: 'Zhodnocení vnitřního i vnějšího prostředí, architektura a design. Možnosti integrace a implementace. Zhodnocení varianty on premise vs. cloud a posouzení, zda půjde o řešení standardní či na míru.',
                step3: 'Vypracování přehledu toho, jaké řešení a technologie jsou na trhu dostupné, jaké jsou lokální reference, dodavatelé, ceny a podmínky dodání. Studii dodáváme v požadovaném rozsahu podle Vámi stanovených kritérií.',
                step4: 'Vypracování poptávky a sběr dat o podmínkách dodání od Vámi vybraného počtu potenciálních dodavatelů. Celé na základě Vámi zadaných kritérií za cílem získání těch nejlepších podmínek.',
                step5: 'Testování a možnosti trial/pilot provozu v rámci daného prostředí. Posouzení funkcionality a technologie v kontextu provozu. Posouzení obchodních a finančních aspektů. Srovnání nabídek, vyjednávání a doporučení pro finální výběr.',
                step6: 'Ustanovení projektového teamu, implementační scénář, implementace a vyhodnocení. Zde je možné doplnění Vašeho projektového teamu (ať už vlastního či dodavatelského) experty z Direct IT.',
            },
            subheadings: {
                project_create: 'Tato sekce představuje výchozí bod pro zadání k novému projektu. Tím může být například nákup nové SW technologie, kde jsou potřeba nezávislé informace z trhu o možných řešeních a dodavatelích a požadavek na obchodní asistenci, ale stejně tak komplexní zadání pro řešení nového informačního systému, kde je potřeba doplnit expertizu v rámci projektového teamu či cokoliv dalšího.',
                project_list: 'Tato sekce přináší komplexní přehled plánovaných projektu a jejich hlavní parametry. Ke každému projektu je zde možné se rychle vrátit, zadat nové skutečnosti a vyžádat nové podklady, informace či další asistenci.',
                software_create: 'Tato sekce umožňuje zadávat prvky Vaší IT infrastruktury, tak jak jsou momentálně využívány. U každé technologie lze aktivovat funkci hlídání expirace, potřeby rozšíření, customizace a další. Team Direct IT pro Vás tak může v pravý čas připravit příslušnou asistenci a zasílat upozornění.',
                software_list: 'Tato sekce nabízí ucelený přehled aktuálně využívaných technologií spolu s aktivitami, které jsou u každé do budoucna plánovány. Díky zadaným parametrům lze rychle poptat příslušnou asistenci a zdroje, které jsou potřeba. '
            },
            dropzone: {
                zone_message: 'Přetažením nebo kliknutím nahrajete soubory'
            },
            datetime: {
                before: {
                    title: 'před',
                    seconds: {
                        singular: 'sekundou',
                        plural: 'sekundami',
                    },
                    minutes: {
                        singular: 'minutou',
                        plural: 'minutami',
                    },
                    hours: {
                        singular: 'hodinou',
                        plural: 'hodinami',
                    },
                    days: {
                        singular: 'dnem',
                        plural: 'dny',
                    },
                    months: {
                        singular: 'měsícem',
                        plural: 'měsíci',
                    },
                    years: {
                        singular: 'rokem',
                        plural: 'roky',
                    },
                }
            },
            files: {
                limit: 'Maximální velikost přílohy je 25 MB.'
            },
            disclaimer: {
                technology_info: 'Informace o Vašich technologiích nejsou komukoliv zpřístupněny a slouží pouze pro účely Vaší soukromé evidence, notifikace a iniciace nových projektů a dalších úkonů spojených se správou dat a Vašeho IT.',
                security_info: 'Jako provozovatelé této platformy bereme ochranu vašich osobních údajů a dat velmi vážně. S veškerými daty zacházíme jako s důvěrnými a nakládáme s nimi v souladu s nařízením o ochraně údajů a podmínkami našeho prohlášení o ochraně dat. Veškerá data jsou šifrována dle standardu AES256.',
            },
        });
    });
};
