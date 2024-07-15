// Properties.jsx
import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./Properties.css";
import { productData } from "../Home/data"; // Import productData from data.js

function Properties() {
  const [properties, setProperties] = useState([]);
  const [handle, setHandle] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");

  useEffect(() => {
    // Initially, set properties to the entire productData array
    setProperties(productData);
  }, []);

  useEffect(() => {
    fetchData();
  }, [searchTerm]);

  const fetchData = () => {
    // Simulate fetching data from an API (in your case, productData is a static array)
    const filteredData = productData.filter((property) =>
      property.location.toLowerCase().includes(searchTerm.toLowerCase())
    );
    setProperties(filteredData);
  };

  const handleSearch = () => {
    fetchData();
  };

  const handleClick = (propertyid) => {
    setHandle((properties) => {
      if (properties.includes(propertyid)) {
        return properties.filter((id) => id !== propertyid);
      } else {
        return [...properties, propertyid];
      }
    });
  };

  return (
    <>
      <h1>Properties</h1>
      <div className="search-field">
        <input
          className="input-field"
          type="text"
          placeholder="Search by location"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <button className="search-btn" onClick={handleSearch}>
          Search
        </button>
      </div>
      <div className="properties--1">
        {properties.map((property) => (
          <div className="item" key={property.id}>
            <img src={property.imageurl} alt={`House ${property.id}`} />
            <h4>Location: {property.location}</h4>
            <h4>Price: {property.price}</h4>
            <button id="btn-seemore">
              <Link to={`/details/${property.id}`} className="seemore--btn">
                See More
              </Link>
            </button>
          </div>
        ))}
      </div>
    </>
  );
}

export default Properties;
