# Function map (auto-generated)

Exact line spans + class context + signature summary for every function in the active build. Use this to jump straight to the lines that implement any behaviour. Line numbers shift as the script evolves — if a span looks off, grep the symbol name.

- `autosp main branch v6.py` — the main script (GUI + engine)
- `autosp mainbranch v3.py` — backend, loaded in-process (read-only)

Regenerate: `python tools/gen_function_map.py`


## autosp main branch v6.py (7949 lines, 22 top-level defs, 2 classes)

- **`_startup_error_file`** `_startup_error_file()` — lines 41–45
- **`_write_startup_error`** `_write_startup_error(exc)` — lines 48–54
- **`_global_excepthook`** `_global_excepthook(etype, evalue, etb)` — lines 57–60
- **`_load_backend`** `_load_backend()` — lines 97–203
- **`_parse_uptime_secs`** `_parse_uptime_secs(s)` — lines 286–300
- **`_summary_uptime_secs`** `_summary_uptime_secs(path)` — lines 303–313
- **`_tracked_vnums_for_bot`** `_tracked_vnums_for_bot(bot_name)` — lines 316–330
- **`_sorted_summary_items`** `_sorted_summary_items(items, tracked)` — lines 333–340
  *nested inside:*
  - **`_key`** `_key(kv)` — lines 337–339
- **`_write_totals_file_uptime`** `_write_totals_file_uptime(path, label, items, gold, uptime_secs, bot_name=None)` — lines 343–367
- **`_pickup_bot_fold`** `_pickup_bot_fold(bot_dir)` — lines 370–529
- **`fold_pickup_summaries`** `fold_pickup_summaries(base_dir=None)` — lines 532–550
- **`_discord_webhook_url`** `_discord_webhook_url(profile_name=None)` — lines 560–569
- **`_send_daily_pickup_webhook`** `_send_daily_pickup_webhook(base_dir=None)` — lines 572–636 · Send yesterday's completed pickup totals to the configured Discord
- **`write_and_fold_pickup_summaries`** `write_and_fold_pickup_summaries(bots)` — lines 641–677
- **`_load_vnums_db`** `_load_vnums_db()` — lines 680–708
- **`_dump_vnums_file`** `_dump_vnums_file(vnums)` — lines 711–738
- **`_hsv_hex`** `_hsv_hex(h, s, v)` — lines 4532–4552 · Convert HSV (h in 0..1, s/v in 0..1) to a '#rrggbb' colour string.
- **`_is_admin`** `_is_admin()` — lines 7653–7658
- **`_relaunch_elevated`** `_relaunch_elevated()` — lines 7661–7681 · Re-launch as Administrator. v3 (when launched by 'START ALL') also
- **`_license_gate`** `_license_gate()` — lines 7684–7861 · License enforcement on startup. Returns a dict with:
  *nested inside:*
  - **`_refuse`** `_refuse(title, msg)` — lines 7713–7720
  - **`submit`** `submit(*_)` — lines 7806–7827
  - **`on_close`** `on_close()` — lines 7835–7837
- **`main`** `main()` — lines 7864–7881
- **`_main`** `_main()` — lines 7884–7907

### class `BackendManager` — lines 756–4512

- **`__init__`** `__init__(self)` — lines 757–785
- **`_pickup_blacklisted`** `_pickup_blacklisted(self, vnum)` — lines 787–795 · True if an item with this vnum must be hidden from pickup stats.
- **`_vnum_name_map`** `_vnum_name_map(self)` — lines 797–840 · Global item vnum -> name map aggregated from every connected bot's
- **`_name_vnum_map`** `_name_vnum_map(self, bot)` — lines 842–873 · Best-effort item name -> vnum map for a bot, from the drop cache,
- **`connect_all`** `connect_all(self)` — lines 876–1167
  *nested inside `connect_all`:*
  - **`_connect`** `_connect(idx_port)` — lines 883–1148
- **`_profile_is_complete`** `_profile_is_complete(self, name)` — lines 1170–1178 · A profile is 'completely set up' if it has a main whose config
- **`_best_complete_profile`** `_best_complete_profile(self)` — lines 1180–1187 · Return the most complete profile to auto-load, or None.
- **`apply_profile`** `apply_profile(self, profile_name=None)` — lines 1189–1255 · Map connected bots into main/child roles from a saved profile.
- **`_propagate_expected_map`** `_propagate_expected_map(self, main_bots)` — lines 1257–1283 · Per-group: each main's expected_map is pushed to ITS OWN children
- **`_wire_group_state`** `_wire_group_state(self)` — lines 1285–1315 · Give every display BotInstance the group/leader links that v3's main()
- **`_build_groups`** `_build_groups(self, main_bots, cached=None)` — lines 1317–1346
- **`autoload_profile`** `autoload_profile(self)` — lines 1348–1350
- **`bots_by_role`** `bots_by_role(self, role)` — lines 1353–1354
- **`mains`** `mains(self)` — lines 1356–1371
- **`children`** `children(self)` — lines 1373–1374
- **`start_all`** `start_all(self)` — lines 1376–1394
- **`_main_config`** `_main_config(self, bot)` — lines 1396–1405
- **`stop_all`** `stop_all(self)` — lines 1407–1415
- **`v3_alive`** `v3_alive(self)` — lines 1422–1426
- **`_v3_set_last_profile`** `_v3_set_last_profile(self)` — lines 1428–1443 · (no longer used to force boot) Keep for compatibility.
- **`_existing_v3_pid`** `_existing_v3_pid(self)` — lines 1445–1465 · Return the pid of an already-running v3 automation process launched
- **`launch_v3`** `launch_v3(self)` — lines 1467–1491
- **`stop_v3`** `stop_v3(self)` — lines 1493–1520
- **`start_bot`** `start_bot(self, bot)` — lines 1522–1550
- **`stop_bot`** `stop_bot(self, bot)` — lines 1552–1567
- **`transform_partner`** `transform_partner(self, bot)` — lines 1569–1578
- **`transform_sp`** `transform_sp(self, bot)` — lines 1580–1587
- **`cmd_transform_all_sp`** `cmd_transform_all_sp(self)` — lines 1591–1613 · G: manually transform every untransformed specialist (mains + children).
- **`cmd_transform_all_partners`** `cmd_transform_all_partners(self)` — lines 1615–1640 · H: manually transform every untransformed partner (mains + children).
- **`inventory_items_list`** `inventory_items_list(self, main_name)` — lines 1642–1674 · Return a grouped inventory listing for a main bot, grouped by
- **`_inventory_grid`** `_inventory_grid(self, main_name)` — lines 1676–1706 · Return per-bag grid layout for a main: {bag: {cols, rows, capacity,
  *nested inside `_inventory_grid`:*
  - **`grid_cols`** `grid_cols(c)` — lines 1693–1697
- **`cmd_debug_force_dump`** `cmd_debug_force_dump(self, picks=None, main_names=None, child_by_main=None)` — lines 1708–1729 · F7 debug: arm a forced inventory dump as if the inventory were full.
- **`cmd_debug_clear_force`** `cmd_debug_clear_force(self)` — lines 1731–1736
- **`cmd_toggle_smart_dump`** `cmd_toggle_smart_dump(self, state=None)` — lines 1738–1751 · Toggle the smart-dump fallback (drop items a child already has).
- **`_ensure_transforms`** `_ensure_transforms(self, bot)` — lines 1753–1766 · Transform SP (G) and partner (H) for a bot if not already up, used
- **`toggle_main_bots`** `toggle_main_bots(self)` — lines 1768–1821 · F5: plain toggle of all main bots. Stop uses type 11 (stop_bot).
- **`status_refresh_loop`** `status_refresh_loop(self, stop_event)` — lines 1831–1847
- **`_engine_const`** `_engine_const(self, name, default)` — lines 1853–1858
- **`_bot_xy`** `_bot_xy(self, bot)` — lines 1860–1873 · Return (x, y, map_id) for a bot, or None if player_data is not
- **`_engine_track_stall`** `_engine_track_stall(self, bot, now)` — lines 1875–1904 · Track a main bot's X/Y and flag it when it has been sitting at the
- **`_can_send_keys`** `_can_send_keys(self, bot)` — lines 1906–1907
- **`_send_input_key`** `_send_input_key(self, scan, hold=0.06)` — lines 1909–1946 · Send a REAL global keystroke via SendInput (scan-code based, no VK
- **`_engine_transform_sp`** `_engine_transform_sp(self, bot)` — lines 1948–1963
- **`_engine_transform_partner`** `_engine_transform_partner(self, bot)` — lines 1965–2053
- **`_engine_partner_suppressed`** `_engine_partner_suppressed(self, bot)` — lines 2055–2070 · True when we must NOT auto-press H for this bot.
- **`_engine_partner_grace_ok`** `_engine_partner_grace_ok(self, bot, now)` — lines 2072–2154 · Return True when it is safe to press H for this bot's partner.
- **`_child_partner_trust_expired`** `_child_partner_trust_expired(self, bot, now)` — lines 2156–2183 · True when a child's optimistic partner trust (set after one H press)
- **`_engine_human_step`** `_engine_human_step(self, bot)` — lines 2185–2279 · Humanized pacing for a main bot. Counts return-amulet uses by an
- **`_engine_step_main`** `_engine_step_main(self, bot)` — lines 2281–2717
- **`_engine_step_child`** `_engine_step_child(self, bot)` — lines 2719–2767
- **`_engine_poll_queries`** `_engine_poll_queries(self, bot)` — lines 2769–2801 · Replicate v3's per-bot periodic queries (player/skills/nearby) and the
- **`_capture_pickup_history`** `_capture_pickup_history(self, bot)` — lines 2803–2947 · Map live 'get' (item pickup) drop objects to item NAMES by diffing the
- **`_engine_manage_groups`** `_engine_manage_groups(self)` — lines 2949–3096 · Replicate v3's group management (invite via chat + accept) inside the
- **`_engine_loop`** `_engine_loop(self)` — lines 3098–3132
- **`_apply_safety_policy`** `_apply_safety_policy(self)` — lines 3134–3195
- **`_safe_close_game`** `_safe_close_game(bot)` — lines 3198–3214
- **`_handle_map_return`** `_handle_map_return(self, bot)` — lines 3216–3233
- **`_dump_config`** `_dump_config(self)` — lines 3238–3266 · Return the dump settings block. If it is missing (or was wiped by a
- **`_human_enabled`** `_human_enabled(self, name)` — lines 3268–3276 · Return whether HUMANIZED pacing is on for the given main group.
- **`_dump_child_free_slots`** `_dump_child_free_slots(self, child, bag=None)` — lines 3278–3286
- **`_dump_press_child_pickup`** `_dump_press_child_pickup(self, child)` — lines 3288–3308 · Press X in the child's game window so it picks up the drops.
- **`_dump_child_pickup_verified`** `_dump_child_pickup_verified(self, st)` — lines 3310–3333 · True once the current child's inventory shows the items dropped in
- **`_dump_should_start`** `_dump_should_start(self, bot)` — lines 3335–3353
- **`_dump_pick_children`** `_dump_pick_children(self, bot, bag=None)` — lines 3355–3386 · Return the usable children for this main, in preference order.
- **`_dump_next_child`** `_dump_next_child(self, bot, st, bag=None)` — lines 3388–3400 · After the current child fills up, return the next child (from the
- **`_dump_select_items`** `_dump_select_items(self, bot, children)` — lines 3402–3561
- **`_dump_start`** `_dump_start(self, bot)` — lines 3563–3615
- **`_dump_advance`** `_dump_advance(self, bot)` — lines 3617–3772
- **`_dump_consume_cannot_drop`** `_dump_consume_cannot_drop(self, bot, st)` — lines 3774–3815 · Handle a server 'cannot drop' sayi ('sayi 1 <id> 10 114 ...') that
- **`_dump_finish`** `_dump_finish(self, bot)` — lines 3817–3836
- **`_engine_dump_step`** `_engine_dump_step(self, bot)` — lines 3838–3856 · Handle a main bot's inventory-dump cycle. Returns True if a dump is
- **`engine_start`** `engine_start(self)` — lines 3858–3867
- **`engine_stop`** `engine_stop(self)` — lines 3869–3889
- **`engine_disconnect`** `engine_disconnect(self)` — lines 3891–3903 · Stop the in-process engine loop WITHOUT sending stop_bot to the
- **`send_key`** `send_key(self, bot, key)` — lines 3914–3922
- **`set_config_dir`** `set_config_dir(self, path)` — lines 3925–3943 · Set the Phoenix (Nostale) config directory: where the per-bot .ini
- **`get_config_dir`** `get_config_dir(self)` — lines 3945–3949
- **`list_ini_configs`** `list_ini_configs(self)` — lines 3951–3959
- **`pull_inventory_names`** `pull_inventory_names(self, bot)` — lines 3961–3987 · Return {bag_type: [(vnum, name), ...]} with the items currently in the
- **`build_profile`** `build_profile(self, profile_name, main_assignments)` — lines 3989–4102 · main_assignments: {bot_name: {'config': path, 'expected_map': int|None,
- **`remove_profile`** `remove_profile(self, profile_name)` — lines 4104–4115
- **`rename_profile`** `rename_profile(self, old_name, new_name)` — lines 4117–4146 · Rename a saved profile key in config.json (keeps its entries), and
- **`reorder_groups`** `reorder_groups(self, ordered_names)` — lines 4148–4196 · Persist a new main-group display order (list of main names, top to
- **`remove_group`** `remove_group(self, main_name)` — lines 4198–4244 · Remove a WHOLE main group (main + its children) from the current
- **`clear_assignment`** `clear_assignment(self)` — lines 4246–4256 · Reset all in-memory role state so the bots window/counters reflect
- **`update_main_config`** `update_main_config(self, main_name, config_path, expected_map=None)` — lines 4258–4278 · Update the profile's main entry with a chosen .ini config + map.
- **`uptime`** `uptime(self, bot)` — lines 4281–4295 · Active-run uptime: only time while this bot's `bot_running` flag is
- **`transform_status`** `transform_status(self, bot)` — lines 4297–4306
- **`sp_status`** `sp_status(self, bot)` — lines 4308–4313
- **`partner_status`** `partner_status(self, bot)` — lines 4315–4345
- **`group_status`** `group_status(self, bot)` — lines 4347–4373
- **`gold`** `gold(self, bot)` — lines 4375–4377
- **`inventory_status`** `inventory_status(self, bot)` — lines 4379–4388 · Return per-bag slot usage for a bot as a tuple
- **`fmt_gold`** `fmt_gold(n)` — lines 4391–4410 · Compact gold formatting: 100000 -> 100k, 2000000 -> 2kk,
- **`drops`** `drops(self, bot)` — lines 4412–4441 · Per-name cumulative pickup counts for a bot, ONLY for items the user
- **`owning_main_name`** `owning_main_name(self, bot)` — lines 4443–4455 · Return the name of the MAIN that owns this bot (itself if the bot is
- **`tracked_items_for_main`** `tracked_items_for_main(self, main_name)` — lines 4457–4475 · Per-main tracked vnum set for one main bot. Reads the dedicated
- **`save_tracked_items_for_main`** `save_tracked_items_for_main(self, main_name, vnums)` — lines 4477–4512 · Persist a main's tracked vnums into the dedicated per-main dict

### class `CommandCentral` — lines 4555–7648

- **`__init__`** `__init__(self, mgr: BackendManager, lic=None)` — lines 4556–4591
- **`build`** `build(self, app)` — lines 4594–4631
- **`_build_header`** `_build_header(self)` — lines 4633–4679
- **`_drag_start`** `_drag_start(self, event)` — lines 4682–4684
- **`_drag_move`** `_drag_move(self, event)` — lines 4686–4700
- **`_drag_stop`** `_drag_stop(self, event)` — lines 4702–4703
- **`_make_draggable`** `_make_draggable(self, widget)` — lines 4705–4718 · Let the given widget (and its transparent children) move the
- **`_build_left`** `_build_left(self)` — lines 4720–4762
- **`_build_right`** `_build_right(self)` — lines 4764–4896
- **`_cmd_pick_items`** `_cmd_pick_items(self)` — lines 4901–4913
- **`_render_pick_choose`** `_render_pick_choose(self, container)` — lines 4915–4935
- **`_pick_main`** `_pick_main(self, main_name)` — lines 4937–4955
- **`_render_pick_tabs`** `_render_pick_tabs(self, container)` — lines 4958–4998
- **`_pick_select_tab`** `_pick_select_tab(self, bag)` — lines 5000–5002
- **`_render_pick_items`** `_render_pick_items(self, container)` — lines 5004–5086
- **`_pick_confirm_tab`** `_pick_confirm_tab(self)` — lines 5088–5102 · Merge the checked items of the current tab into the running
- **`_pick_back_to_tabs`** `_pick_back_to_tabs(self)` — lines 5104–5106
- **`_save_pick_selection`** `_save_pick_selection(self)` — lines 5108–5114
- **`_pick_done`** `_pick_done(self)` — lines 5116–5128 · Finish the picker: persist the running selection, refresh the filter
- **`_pick_cancel`** `_pick_cancel(self)` — lines 5130–5135
- **`_settle_scroll`** `_settle_scroll(self, container)` — lines 5137–5148 · Recompute the scrollable frame's canvas scrollregion so it matches
- **`_render_bots`** `_render_bots(self)` — lines 5151–5303
- **`_make_group_draggable`** `_make_group_draggable(self, widget, main_name)` — lines 5306–5320 · Bind a widget (and its children) to the group reorder/trash drag so
- **`_group_row_hit`** `_group_row_hit(self, x_root, y_root)` — lines 5322–5338 · Return the main name whose group row contains this screen point, or
- **`_group_trash_hit`** `_group_trash_hit(self, x_root, y_root)` — lines 5340–5350 · Return the main name of the trash button under this screen point.
- **`_group_drag_start`** `_group_drag_start(self, event, main_name)` — lines 5352–5356
- **`_group_drag_move`** `_group_drag_move(self, event)` — lines 5358–5382
- **`_group_drag_stop`** `_group_drag_stop(self, event)` — lines 5384–5409
- **`_cmd_move_group`** `_cmd_move_group(self, main_name, delta, target=None)` — lines 5411–5430 · Move a main group up (delta -1), down (+1), or directly before/after
- **`_cmd_remove_group`** `_cmd_remove_group(self, main_name)` — lines 5432–5439
- **`_assign_claimed`** `_assign_claimed(self, name)` — lines 5442–5455 · Is a bot already claimed by a saved group? Only bots actually
- **`_toggle_assign`** `_toggle_assign(self)` — lines 5457–5476
- **`_render_assign`** `_render_assign(self, container)` — lines 5478–5547
- **`_click_assign`** `_click_assign(self, name)` — lines 5549–5567
- **`_apply_grouping`** `_apply_grouping(self)` — lines 5569–5594
- **`_render_cfg_inline`** `_render_cfg_inline(self, container, main_name)` — lines 5597–5733
  *nested inside `_render_cfg_inline`:*
  - **`save`** `save()` — lines 5692–5719
  - **`skip`** `skip()` — lines 5721–5725
- **`_cfg_cancel`** `_cfg_cancel(self)` — lines 5735–5739
- **`_pick_config_dir`** `_pick_config_dir(self)` — lines 5741–5764 · Open a folder picker for the Phoenix/Nostale config directory (the
- **`_cfg_map_choices`** `_cfg_map_choices(self)` — lines 5767–5782 · Build the (labels, ids) option lists for the expected-map dropdown.
- **`_cfg_map_refresh`** `_cfg_map_refresh(self)` — lines 5784–5807 · Refresh the live map dropdown + per-bot current-map readout every
- **`_cfg_stop_map_refresh`** `_cfg_stop_map_refresh(self)` — lines 5809–5816
- **`_make_stat`** `_make_stat(self, parent, label, color=THEME['muted'])` — lines 5818–5825 · A status chip: just the label text, whose COLOUR shows the state
- **`_power_button`** `_power_button(self, parent, bot)` — lines 5827–5844 · A small circular power button. Green when the bot is running, dim
  *nested inside `_power_button`:*
  - **`on`** `on()` — lines 5830–5835
- **`_refresh_power_buttons`** `_refresh_power_buttons(self)` — lines 5846–5858 · Static pass: dim the button when the bot is off. When the bot is
- **`_animate_tick`** `_animate_tick(self)` — lines 5860–5908 · Lightweight UI animation loop (runs on the Tk main thread): slowly
- **`_refresh`** `_refresh(self)` — lines 5911–5952
- **`_update_values`** `_update_values(self)` — lines 5954–5994
- **`_poll_skills`** `_poll_skills(self)` — lines 5996–6008 · Background (non-UI) skill refresh so the UI thread never blocks on
- **`_init_stat_tags`** `_init_stat_tags(widget, owner=None)` — lines 6012–6049
  *nested inside `_init_stat_tags`:*
  - **`_hover`** `_hover(e)` — lines 6038–6047
- **`_cycle_stats_bot`** `_cycle_stats_bot(self)` — lines 6051–6065
- **`_cycle_filter_bot`** `_cycle_filter_bot(self)` — lines 6067–6079
- **`_flash_filter_header`** `_flash_filter_header(self)` — lines 6081–6091
- **`_flash_stats_name`** `_flash_stats_name(self)` — lines 6093–6110
- **`_refresh_stats_now`** `_refresh_stats_now(self)` — lines 6112–6119
- **`_stats_segments`** `_stats_segments(self)` — lines 6121–6200
- **`_live_get_log`** `_live_get_log(self, bot)` — lines 6202–6278 · Return a rolling list of (timestamp, object_id, mapped_name) for the
- **`_set_text`** `_set_text(cls, widget, value, last=None)` — lines 6281–6305
- **`_cmd_start_all`** `_cmd_start_all(self)` — lines 6309–6323
  *nested inside `_cmd_start_all`:*
  - **`_go`** `_go()` — lines 6310–6320
- **`_cmd_stop_all`** `_cmd_stop_all(self)` — lines 6325–6330
  *nested inside `_cmd_stop_all`:*
  - **`_go`** `_go()` — lines 6326–6328
- **`_cmd_toggle_smart`** `_cmd_toggle_smart(self)` — lines 6332–6343
  *nested inside `_cmd_toggle_smart`:*
  - **`_go`** `_go()` — lines 6333–6342
- **`_set_smart_btn`** `_set_smart_btn(self, label, fg, txt, hv, state)` — lines 6345–6357
- **`_render_fast_dump_btn`** `_render_fast_dump_btn(self, parent, main)` — lines 6360–6390 · Build the AUTO DUMP on/off button for a main group. It is a master
  *nested inside `_render_fast_dump_btn`:*
  - **`on`** `on()` — lines 6364–6365
- **`_cmd_human_toggle`** `_cmd_human_toggle(self, main)` — lines 6392–6402 · Toggle HUMANIZED pacing for a main group (randomized stop/resume).
- **`_refresh_human_buttons`** `_refresh_human_buttons(self)` — lines 6404–6417 · Sync all HUMAN buttons to the current per-main state.
- **`_cmd_fast_dump_toggle`** `_cmd_fast_dump_toggle(self, main)` — lines 6419–6447 · Toggle AUTO DUMP for a main and reveal the dump config panel
- **`_refresh_fast_dump_buttons`** `_refresh_fast_dump_buttons(self)` — lines 6449–6463 · Sync all AUTO DUMP buttons to the current master state.
- **`_build_fast_drop_panel`** `_build_fast_drop_panel(self)` — lines 6465–6562 · Build the AUTO DUMP panel (lower half of the BOTS column). It hosts
  *nested inside `_build_fast_drop_panel`:*
  - **`_fd_stretch`** `_fd_stretch(e=None)` — lines 6525–6535
  - **`_fd_poll`** `_fd_poll()` — lines 6537–6543
- **`_render_force_dump_inline`** `_render_force_dump_inline(self, container)` — lines 6564–6996 · Render the AUTO DUMP config: per-main target child picker, item
  *nested inside `_render_force_dump_inline`:*
  - **`confirm`** `confirm()` — lines 6926–6978
  - **`dump_now`** `dump_now()` — lines 6980–6991
- **`_cmd_fast_drop_collapse`** `_cmd_fast_drop_collapse(self)` — lines 6998–7013 · Hide the AUTO DUMP panel again and let the BOTS list fill the column.
- **`_cmd_start_bot`** `_cmd_start_bot(self, bot)` — lines 7015–7017
- **`_cmd_stop_bot`** `_cmd_stop_bot(self, bot)` — lines 7019–7021
- **`_cmd_profile`** `_cmd_profile(self, name)` — lines 7023–7035
- **`_new_profile`** `_new_profile(self)` — lines 7037–7038
- **`_cmd_new_config`** `_cmd_new_config(self)` — lines 7040–7041
- **`_cmd_edit_config`** `_cmd_edit_config(self)` — lines 7043–7044
- **`_cmd_remove_config`** `_cmd_remove_config(self)` — lines 7046–7068 · Red button: remove the currently selected config profile.
- **`_rename_cfg_inline`** `_rename_cfg_inline(self)` — lines 7070–7122 · Right-click the current config label: swap it for an inline entry to
- **`_webhook_dialog`** `_webhook_dialog(self)` — lines 7124–7194 · Double-click the current config profile: set (or clear) a Discord
- **`_redraw_cfg_card`** `_redraw_cfg_card(self)` — lines 7196–7206 · Force the config card to re-render its rounded border. Dynamically
- **`_config_dialog`** `_config_dialog(self, new_profile=True)` — lines 7208–7360 · Build/edit a profile: pick which bots are MAIN, choose their config
  *nested inside `_config_dialog`:*
  - **`_dlg_map_tick`** `_dlg_map_tick()` — lines 7273–7288 · Live-refresh every row's map dropdown + current-map readout while
  - **`_dlg_pick_cfg_dir`** `_dlg_pick_cfg_dir()` — lines 7290–7315 · Pick the Phoenix/Nostale config dir and refresh the dialog's
  - **`save`** `save()` — lines 7321–7353
- **`_load_profiles`** `_load_profiles(self, select=None)` — lines 7362–7370
- **`_cmd_apply_filters`** `_cmd_apply_filters(self)` — lines 7372–7387 · Re-apply the per-main tracked vnum lists (already saved live by the
- **`_remove_filter_item`** `_remove_filter_item(self, main_name, vnum)` — lines 7389–7400 · ✕ button on an ITEM FILTERS row: remove that one vnum from the main's
- **`_status`** `_status(self, bots, msg)` — lines 7402–7404
- **`_populate_filters`** `_populate_filters(self)` — lines 7407–7489 · Render the ITEM FILTERS card for the currently selected mainbot, just
- **`run`** `run(self)` — lines 7491–7583
  *nested inside `run`:*
  - **`_startup`** `_startup()` — lines 7495–7523
  - **`_child_loop`** `_child_loop()` — lines 7532–7533
- **`_post_connect`** `_post_connect(self)` — lines 7585–7597
- **`_key_loop`** `_key_loop(self)` — lines 7599–7648 · Global hotkey handler thread.

## autosp mainbranch v3.py (5525 lines, 61 top-level defs, 2 classes)

- **`ensure_psutil`** `ensure_psutil()` — lines 22–31
- **`load_config`** `load_config()` — lines 45–52
- **`save_config`** `save_config(cfg)` — lines 54–61
- **`load_settings`** `load_settings()` — lines 63–64
- **`save_settings`** `save_settings(settings)` — lines 66–69
- **`log_debug`** `log_debug(msg)` — lines 109–121
- **`save_get_map`** `save_get_map()` — lines 157–163
- **`human_sleep`** `human_sleep(min_sec: float=1.0, max_sec: float=2.0)` — lines 167–168
- **`is_admin`** `is_admin()` — lines 172–176
- **`elevate`** `elevate()` — lines 177–184
- **`hue_to_rgb`** `hue_to_rgb(hue: float)` — lines 209–218
- **`rgb_escape`** `rgb_escape(r, g, b)` — lines 220–221
- **`_t`** `_t(name, default)` — lines 242–243
- **`bring_window_foreground`** `bring_window_foreground(hwnd)` — lines 325–355
- **`press_key_escape`** `press_key_escape()` — lines 357–361
- **`send_key_direct`** `send_key_direct(hwnd, scan)` — lines 363–380 · Send a key down/up straight to a game window without stealing focus.
- **`press_key_to`** `press_key_to(hwnd, scan, unload_first=False)` — lines 382–398 · Press a key. If DIRECT_KEY_SEND is on and we have a window, post the
- **`press_key_g`** `press_key_g(hwnd=0)` — lines 400–401
- **`press_key_h`** `press_key_h(hwnd=0)` — lines 403–404
- **`press_key_s`** `press_key_s(hwnd=0)` — lines 406–407
- **`press_key_d`** `press_key_d(hwnd=0)` — lines 409–410
- **`press_key_enter`** `press_key_enter(hwnd=0)` — lines 412–413
- **`press_s_to_stop`** `press_s_to_stop(bot)` — lines 415–427
- **`cancel_movement_api`** `cancel_movement_api(bot)` — lines 429–437
- **`keys_to_bot_ready`** `keys_to_bot_ready(bot)` — lines 439–444 · True if we can send keys to this bot: either direct-posting (no focus
- **`press_key_num`** `press_key_num(num)` — lines 446–456
- **`get_windows_info`** `get_windows_info()` — lines 462–495
  *nested inside:*
  - **`callback`** `callback(hwnd, lParam)` — lines 466–491
- **`get_process_id_for_port`** `get_process_id_for_port(port: int)` — lines 501–509
- **`get_game_hwnd_for_port`** `get_game_hwnd_for_port(port: int)` — lines 511–532
  *nested inside:*
  - **`enum_callback`** `enum_callback(hwnd, lParam)` — lines 517–529
- **`format_drops_block`** `format_drops_block(bots)` — lines 3107–3129 · Per-item pickup counts (aggregated across bots), for display under the
- **`start_skill_cycle`** `start_skill_cycle(bot)` — lines 3136–3196
  *nested inside:*
  - **`attack_loop`** `attack_loop()` — lines 3147–3191
- **`stop_skill_cycle`** `stop_skill_cycle(bot)` — lines 3198–3211
- **`start_attack_mode`** `start_attack_mode(bot)` — lines 3213–3221
- **`stop_attack_mode`** `stop_attack_mode(bot)` — lines 3223–3232
- **`assign_group_leaders`** `assign_group_leaders(all_bots, main_bot_objects)` — lines 3240–3293
- **`add_main_bot_interactive`** `add_main_bot_interactive(all_bots, main_bot_objects, main_bots, ordered_bots, leader, leader_name, leader_id, main_started_flags, started_bots, map_check_enabled, bot_running_global, main_sp_attempts, main_partner_attempts, skill_active, skill_threads)` — lines 3296–3493
- **`load_cache`** `load_cache()` — lines 3499–3507
- **`save_cache`** `save_cache(entries)` — lines 3509–3526
- **`list_profiles`** `list_profiles()` — lines 3528–3536
- **`load_cache_profile`** `load_cache_profile(name)` — lines 3538–3544
- **`save_cache_as`** `save_cache_as(entries, name)` — lines 3546–3556
- **`apply_cache_entries`** `apply_cache_entries(player_map, cached)` — lines 3558–3594
- **`switch_config_interactive`** `switch_config_interactive(player_map, main_bots, children)` — lines 3596–3628
- **`_perform_partner_retry`** `_perform_partner_retry(bot)` — lines 3633–3681
- **`inventory_poll_loop`** `inventory_poll_loop(bots: list, interval: float=INVENTORY_POLL_INTERVAL)` — lines 3687–3703
- **`_snapshot_inventory_items`** `_snapshot_inventory_items(bot, bag_type=None)` — lines 3713–3728
- **`_interactive_pick`** `_interactive_pick(entries, label, page_size=20, single=False, show_marks=True, show_hint=True, show_pageinfo=True, show_arrow=True, show_sep=True, allow_space=True, one_based=False, max_select=None)` — lines 3731–3840
  *nested inside:*
  - **`_toggle`** `_toggle(i)` — lines 3754–3766
- **`_choose_tracked_items_paged`** `_choose_tracked_items_paged(entries, label, page_size=20)` — lines 3843–3845
- **`configure_tracked_items`** `configure_tracked_items(bot)` — lines 3848–3889
- **`_fmt_run_uptime`** `_fmt_run_uptime(secs)` — lines 3892–3901
- **`_summary_base_dir`** `_summary_base_dir()` — lines 3903–3905
- **`_compute_bot_gain`** `_compute_bot_gain(main)` — lines 3908–3940
- **`_write_bot_run_summary`** `_write_bot_run_summary(bot, gains, gold_gain)` — lines 3943–3978
- **`dump_pickup_summary`** `dump_pickup_summary(bots)` — lines 3981–4010
- **`_parse_run_summary`** `_parse_run_summary(path)` — lines 4016–4044
- **`_day_key`** `_day_key(end_str)` — lines 4047–4054
- **`_period_label`** `_period_label(d, day=False, week=False, month=False)` — lines 4057–4064
- **`_write_totals_file`** `_write_totals_file(path, label, items, gold)` — lines 4067–4085
- **`_aggregate_bot_folder`** `_aggregate_bot_folder(bot_dir)` — lines 4088–4163
- **`aggregate_pickup_summaries`** `aggregate_pickup_summaries(base_dir=None)` — lines 4166–4183
- **`main`** `main()` — lines 4185–5522
  *nested inside:*
  - **`_connect_one`** `_connect_one(idx_port)` — lines 4209–4248
  - **`can_send_keys`** `can_send_keys(bot)` — lines 4593–4596
  - **`_run_main_bot`** `_run_main_bot(bot)` — lines 4598–4915
  - **`main_bot_worker`** `main_bot_worker()` — lines 4917–4929
  - **`_transform_child_sp`** `_transform_child_sp(bot)` — lines 4935–4946
  - **`_transform_child_partner`** `_transform_child_partner(bot)` — lines 4948–4971
  - **`child_worker`** `child_worker()` — lines 4973–5032
  - **`_watchdog`** `_watchdog()` — lines 5088–5104

### class `PhoenixBotAPI` — lines 538–784

- **`__init__`** `__init__(self, host: str='127.0.0.1', port: Optional[int]=None)` — lines 541–551
- **`_candidate_hosts`** `_candidate_hosts(self)` — lines 553–596
- **`connect`** `connect(self, port: int)` — lines 598–627
- **`close`** `close(self)` — lines 629–636
- **`send`** `send(self, msg_dict: Dict[str, Any])` — lines 638–648
- **`_receive_loop`** `_receive_loop(self)` — lines 650–666
- **`_process_loop`** `_process_loop(self)` — lines 668–680
- **`_dispatch_message`** `_dispatch_message(self, msg: Dict[str, Any])` — lines 682–687
- **`register_callback`** `register_callback(self, callback: callable)` — lines 689–690
- **`set_incoming_sniffer`** `set_incoming_sniffer(self, sniffer: callable)` — lines 692–693
- **`query_player_info`** `query_player_info(self)` — lines 695–696
- **`query_skills`** `query_skills(self)` — lines 698–699
- **`query_inventory`** `query_inventory(self)` — lines 701–702
- **`query_bot_status`** `query_bot_status(self)` — lines 704–705
- **`query_partner_skills`** `query_partner_skills(self)` — lines 707–708
- **`load_config`** `load_config(self, path: str)` — lines 710–712
- **`start_bot`** `start_bot(self)` — lines 714–716
- **`stop_bot`** `stop_bot(self)` — lines 718–720
- **`continue_bot`** `continue_bot(self)` — lines 722–724
- **`use_item`** `use_item(self, character_id: int, bag_type: int, slot: int)` — lines 726–728
- **`drop_item`** `drop_item(self, bag_type: int, slot: int, amount: int=1)` — lines 730–733
- **`send_packet`** `send_packet(self, packet: str)` — lines 735–736
- **`query_nearby_entities`** `query_nearby_entities(self)` — lines 738–740
- **`sniff_send_packets`** `sniff_send_packets(self, filter_str: Optional[str]=None, callback: Optional[callable]=None)` — lines 742–751
  *nested inside `sniff_send_packets`:*
  - **`_sniffer`** `_sniffer(msg)` — lines 743–750
- **`walk_to`** `walk_to(self, x: int, y: int)` — lines 753–755
- **`walk_partner_to`** `walk_partner_to(self, x: int, y: int)` — lines 757–759
- **`attack_monster`** `attack_monster(self, monster_id: int)` — lines 761–764
- **`attack_entity`** `attack_entity(self, entity_id: int)` — lines 766–769
- **`target_entity`** `target_entity(self, entity_id: int, entity_type: int=3)` — lines 771–774
- **`pet_attack`** `pet_attack(self, monster_id: int, skill_id: str='')` — lines 776–779
- **`use_player_skill`** `use_player_skill(self, monster_id: int, skill_id: int)` — lines 781–784

### class `BotInstance` — lines 797–3104

- **`walk_to`** `walk_to(self, x: int, y: int)` — lines 798–799
- **`__init__`** `__init__(self, port: int, api: PhoenixBotAPI)` — lines 800–1014
- **`_cancel_partner_verify`** `_cancel_partner_verify(self)` — lines 1017–1020
- **`_has_recent_partner_proof`** `_has_recent_partner_proof(self)` — lines 1022–1031
- **`_defer_no_partner_loss`** `_defer_no_partner_loss(self)` — lines 1033–1053
- **`_on_partner_loss`** `_on_partner_loss(self)` — lines 1055–1073
- **`_on_partner_ready`** `_on_partner_ready(self)` — lines 1075–1093
- **`discover_pet_attack_skill`** `discover_pet_attack_skill(self, monster_id: Optional[int]=None)` — lines 1095–1141 · Try pet_attack skill ids (blank + small range) until one makes the
- **`set_user_wants_bot_on`** `set_user_wants_bot_on(self, enabled: bool)` — lines 1143–1147
- **`_update_bot_state`** `_update_bot_state(self)` — lines 1149–1163
- **`is_partner_transformed`** `is_partner_transformed(self)` — lines 1165–1178
- **`has_partner_equipped`** `has_partner_equipped(self)` — lines 1180–1181
- **`on_message`** `on_message(self, msg: Dict[str, Any])` — lines 1183–1575
- **`_associate_get_ids`** `_associate_get_ids(self, name, vnum)` — lines 1577–1598 · Attribute a confirmed tracked-item gain to the most recent GET
- **`_process_packet`** `_process_packet(self, packet: str)` — lines 1600–2081
- **`_auto_accept_group_invite`** `_auto_accept_group_invite(self)` — lines 2083–2109
  *nested inside `_auto_accept_group_invite`:*
  - **`_accept`** `_accept()` — lines 2103–2108
- **`_handle_sp_packet`** `_handle_sp_packet(self, packet: str)` — lines 2111–2133
- **`_handle_ski_packet`** `_handle_ski_packet(self, packet: str)` — lines 2135–2153
- **`_classify_sayi`** `_classify_sayi(self, packet: str)` — lines 2155–2192
- **`_process_outgoing_packet`** `_process_outgoing_packet(self, packet: str)` — lines 2194–2292
- **`_parse_pinit`** `_parse_pinit(self, packet: str)` — lines 2294–2332
- **`_handle_infoi`** `_handle_infoi(self, packet: str)` — lines 2334–2400
- **`_propagate_group_info`** `_propagate_group_info(self)` — lines 2402–2427
- **`_scan_for_partner_vnums`** `_scan_for_partner_vnums(self, packet: str)` — lines 2429–2430
- **`_start_clear_timer`** `_start_clear_timer(self)` — lines 2432–2446
- **`_cancel_clear_timer`** `_cancel_clear_timer(self)` — lines 2448–2463
- **`_save_partner_skills_to_cache`** `_save_partner_skills_to_cache(self)` — lines 2465–2488
- **`_save_sp_skills_to_cache`** `_save_sp_skills_to_cache(self, sp_skills)` — lines 2490–2513
- **`force_partner_retry`** `force_partner_retry(self)` — lines 2516–2530
- **`sync_bot`** `sync_bot(self)` — lines 2532–2619
- **`partner_sync_only`** `partner_sync_only(self)` — lines 2621–2673
- **`sp_sync_only`** `sp_sync_only(self)` — lines 2675–2706
- **`is_grouped_with`** `is_grouped_with(self, bot_name: str)` — lines 2709–2714
- **`request_group_info`** `request_group_info(self)` — lines 2716–2721
- **`query_player`** `query_player(self)` — lines 2724–2725
- **`query_skills`** `query_skills(self)` — lines 2727–2729
- **`query_inventory`** `query_inventory(self)` — lines 2731–2732
- **`query_bot_status`** `query_bot_status(self)` — lines 2734–2735
- **`query_nearby`** `query_nearby(self)` — lines 2737–2738
- **`query_partner_skills`** `query_partner_skills(self)` — lines 2740–2741
- **`get_closest_monster`** `get_closest_monster(self)` — lines 2744–2764
- **`update_closest_monster`** `update_closest_monster(self)` — lines 2766–2776
- **`load_and_start`** `load_and_start(self, config_path: str)` — lines 2779–2791
- **`toggle_bot`** `toggle_bot(self)` — lines 2793–2801
- **`check_map_and_return`** `check_map_and_return(self)` — lines 2804–2858
- **`check_death_and_reset`** `check_death_and_reset(self)` — lines 2860–2883
- **`_inventory_timeout`** `_inventory_timeout(self)` — lines 2885–2892
- **`_inv_poll_timeout`** `_inv_poll_timeout(self)` — lines 2894–2896
- **`_process_inventory_for_return`** `_process_inventory_for_return(self)` — lines 2898–2941
- **`confirm_via_keyboard`** `confirm_via_keyboard(self, delay: float=1.0)` — lines 2943–2953
  *nested inside `confirm_via_keyboard`:*
  - **`_confirm`** `_confirm()` — lines 2946–2952
- **`close_game`** `close_game(self)` — lines 2955–2966
- **`_check_partner_timeout`** `_check_partner_timeout(self)` — lines 2968–2986
- **`close`** `close(self)` — lines 2988–2999
- **`get_status_line`** `get_status_line(self)` — lines 3001–3104
