import React from 'react';
import './profile.css';

const Profile = () => {
  return (
    <div className="bg-white p-8 rounded-lg shadow-md">
      <h2 className="text-4xl font-bold mb-6 text-blue-700">Team Profile</h2>
      <p className="text-lg mb-4">
        This project was completed by a dedicated team of four ICT students at NHL Stenden, Emmen.
      </p>
      <p className="text-lg mb-4">
        <strong>Project Owner:</strong> IT Hub
      </p>
      <div className="mb-4">
        <strong className="block text-lg mb-2">Team Members</strong>
        <ul className="list-disc pl-5 space-y-1">
          <li>Bart Wijshake</li>
          <li>Yaëll Kuipers</li>
          <li>Polly Zueva</li>
          <li>Virag Szabo</li>
        </ul>
      </div>
    </div>
  );
};

export default Profile;