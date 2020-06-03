import { h } from 'preact';
import DeptControl from './../DeptControl/index.jsx';
import DeptGroup from './../DeptGroup/index.jsx';


const makeGroup = (slug, departments, name, label, empty) => {
  return (
    <div className="DeptSearch-groupWrap">
      <DeptGroup
        map={slug}
        linksArray={departments}
        label={label}
        name={name}
        empty={empty}
        doubleRow={slug === 'south-africa'}
      />
    </div>
  );
};


const emptyNotification = (
  <div className="Section is-bevel is-dark">
    <div className="Section-card is-invisible">
      <div className="Section-title">
        No results found
      </div>
      <div>
        Please try changing or broadening your search terms
      </div>
    </div>
  </div>
);


const showResults = (results) => {
  const hasItemsInDept = ({ departments }) => departments.length > 0;

  if (results.filter(hasItemsInDept).length < 1) {
    return emptyNotification;
  }

  return results.map(
    ({ name, slug, departments, label }) => {
      const empty = departments.length == 0;
      return makeGroup(slug, departments, name, label, empty);
    },
  );
};


export default function DeptSearchMarkup({ state, eventHandlers }) {
  const { results } = state;

  return (
    <div className="DeptSearch">
      <div className="DeptSearch-wrap">
        <h3 className="u-sReadOnly">Filters</h3>
        <ul className="DeptSearch-list">
          <li>
            <DeptControl
              open={state.open}

              keywords={state.filters.keywords}
              sphere={state.filters.sphere}
              province={state.filters.province}

              updateFilter={eventHandlers.updateDropdown}
              changeKeywords={eventHandlers.updateKeywords}
            />
          </li>
        </ul>
        <h3 className="u-sReadOnly">Results</h3>
        <div className="DeptSearch-results">
          {showResults(results)}
        </div>
      </div>
    </div>
  );
}
