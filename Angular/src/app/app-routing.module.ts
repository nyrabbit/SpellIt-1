import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LanguageListComponent } from './language-list/language-list.component';
import { ParadigmListComponent } from './paradigm-list/paradigm-list.component';
import { LanguageAddComponent } from './language-add/language-add.component';
import { ParadigmEditComponent } from './paradigm-edit/paradigm-edit.component';
import { ParadigmAddComponent } from './paradigm-add/paradigm-add.component';

const routes: Routes = [
  {
    path: '',
    component: LanguageListComponent
  },
  {
    path: 'language-list',
    component: LanguageListComponent
  },
  {
    path: 'language/:language_id',
    component: ParadigmListComponent
  },
  {
    path: 'language/:language_id/:paradigm_id',
    component: ParadigmEditComponent
  },
  {
    path: 'language-add',
    component: LanguageAddComponent
  },
  {
    path: 'paradigm-add',
    component: ParadigmAddComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
