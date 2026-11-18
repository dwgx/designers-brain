/*
 * UI-03 fixture — CounterButton state machine (single source of truth).
 *
 * This is a deliberately small, dependency-free component used to demonstrate
 * LAYERED acceptance: geometry / behavior / semantics are measured separately,
 * and model- or human-aesthetic judgement is NOT claimed by any of them.
 *
 * Works as a classic <script> in the browser AND as a CommonJS module in Node:
 *   browser: window.CounterButton
 *   node:    require('./component.js')
 */
(function (root, factory) {
  'use strict';
  var api = factory();
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.CounterButton = api;
})(typeof globalThis !== 'undefined' ? globalThis : this, function () {
  'use strict';

  function initialState(opts) {
    opts = opts || {};
    return {
      count: 0,
      pressed: false,
      disabled: !!opts.disabled
    };
  }

  /*
   * Pure reducer. `action` is one of:
   *   { type: 'activate', via: 'pointer' | 'keyboard' }
   *   { type: 'setDisabled', value: Boolean }
   *
   * Contract under test:
   *   - activation via pointer OR keyboard increments count by exactly 1 and
   *     toggles aria-pressed;
   *   - when disabled, activation is a no-op (returns the identical state);
   *   - unknown actions are a no-op.
   *
   * This reducer knows NOTHING about pixels, aesthetics, or task goals. A green
   * result here is a BEHAVIOR result, not a quality or human-acceptance result.
   */
  function reduce(state, action) {
    if (!action) return state;
    if (action.type === 'setDisabled') {
      return { count: state.count, pressed: state.pressed, disabled: !!action.value };
    }
    if (action.type === 'activate') {
      if (state.disabled) return state;            // disabled blocks activation
      if (action.via !== 'pointer' && action.via !== 'keyboard') return state;
      return {
        count: state.count + 1,
        pressed: !state.pressed,
        disabled: state.disabled
      };
    }
    return state;
  }

  /* Accessible name is a SEMANTIC property, not a behavior or a pixel property. */
  var ACCESSIBLE_NAME = 'Add one to the counter';

  return {
    initialState: initialState,
    reduce: reduce,
    ACCESSIBLE_NAME: ACCESSIBLE_NAME
  };
});
