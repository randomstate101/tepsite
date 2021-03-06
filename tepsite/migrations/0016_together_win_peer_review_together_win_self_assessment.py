# Generated by Django 2.2 on 2020-06-21 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tepsite', '0015_man_eff_employee_engagement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Together_win_Peer_Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intern_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20, null=True)),
                ('Name_of_your_Teammate', models.CharField(max_length=100)),
                ('Teammate_clearly_understands_the_purpose_of_our_team', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('Teammate_openly_expresses_ideas_and_opinions', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('Teammate_is_able_to_make_thoughtful_decisions_that_all_team_members_support', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('Teammate_trusts_and_respects_other_team_members', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('Teammate_expresses_disagreements_constructively', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('Teammate_willingly_take_on_new_responsibilities', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('Teammate_follow_through_on_decisions_and_action_items', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('Teammate_has_the_necessary_skills_to_carry_out_his_work', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('Teammate_frequently_goes_beyond_what_is_required_and_does_not_hesitate_to_take_initiative', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Together_win_Self_Assessment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intern_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20, null=True)),
                ('My_team_has_a_meaningful_and_shared_purpose', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_clearly_understand_my_role_within_the_team', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('Team_problem_solving_results_in_effective_solutions', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_appreciate_the_unique_capabilities_of_my_team_members', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_take_personal_responsibility_for_the_effectiveness_of_my_team', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('Working_on_my_team_aspires_me_to_do_my_best', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_have_the_skills_I_need_to_do_my_job_for_the_team_effectively', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('My_team_sets_and_meets_challenging_goals', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('When_an_individuals_role_changes_I_make_an_intentional_effort_to_clarify_it_for_everyone_on_the_team', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_address_and_resolve_issues_quickly', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_am_open_and_honest_with_the_communication_in_my_group', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_take_initiative_to_resolve_issues_between_the_team_members_without_involving_the_team_leader', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_have_a_strong_sense_of_accomplishment_regarding_my_work', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_always_ask_myself_How_can_we_do_better_tomorrow_what_we_did_today', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('As_a_part_of_my_team_I_always_produce_strong_measurable_results', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_avoid_duplication_of_efforts_and_make_sure_that_everyone_is_clear_about_who_is_doing_what', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('My_team_has_mechanisms_in_place_to_monitor_its_results', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_trust_the_members_of_my_team', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_spend_very_little_time_complaining_about_things_I_cannot_control', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_frequently_go_beyond_what_is_required_and_do_not_hesitate_to_take_initiative', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('As_a_team_we_are_continually_working_to_improve_key_performance_indicators', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_make_sure_my_work_helps_the_organization_achieve_its_goals', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('When_team_members_roles_change_Specific_plans_are_implemented_to_help_them_assume_their_new_responsibilities', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_work_with_a_great_deal_of_flexibility_so_that_I_can_adapt_to_changing_needs', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_help_other_team_members_deal_with_problems_or_resolve_issues', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_seek_and_give_other_team_members_with_constructive_feedback', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('As_a_team_we_work_to_attract_and_retain_top_performers', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('We_work_to_ensure_that_we_are_using_the_best_practices', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('The_mission_and_goals_of_my_team_are_well_aligned_with_the_organizations_mission_and_goals', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('Overlapping_or_shared_tasks_and_responsibilities_do_not_create_problems_for_team_members', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('When_we_choose_consensus_decision_making_we_do_it_effectively', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_am_able_to_work_through_differences_of_opinion_without_damaging_relationships', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_am_sure_about_what_is_expected_of_me_and_take_pride_in_a_job_well_done', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_am_excited_about_the_contribution_it_is_making_to_the_organizations_competitive_viability', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
                ('I_embrace_continuous_improvement_as_a_way_of_life', models.CharField(blank=True, choices=[('Strongly Disagree', 'Strongly Disagree'), ('Disagree', 'Disagree'), ('Neutral', 'Neutral'), ('Agree', 'Agree'), ('Strongly Agree', 'Strongly Agree')], max_length=25, null=True)),
            ],
        ),
    ]
