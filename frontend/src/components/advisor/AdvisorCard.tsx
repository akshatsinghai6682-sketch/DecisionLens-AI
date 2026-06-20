import React from 'react';
import { Users, AlertCircle } from 'lucide-react';

interface AdvisorCardProps {
  advisorType: string;
  keyConcern: string;
  recommendation: string;
  blindSpot: string;
}

export const AdvisorCard: React.FC<AdvisorCardProps> = ({
  advisorType,
  keyConcern,
  recommendation,
  blindSpot,
}) => {
  const getAdvisorColor = (type: string) => {
    switch (type) {
      case 'Pragmatic Parent':
        return 'border-blue-200 bg-blue-50';
      case 'Risk-Taking Entrepreneur':
        return 'border-orange-200 bg-orange-50';
      case 'Cautious Academic':
        return 'border-green-200 bg-green-50';
      case 'Values-First Counselor':
        return 'border-purple-200 bg-purple-50';
      case 'Data-Driven Analyst':
        return 'border-gray-200 bg-gray-50';
      default:
        return 'border-gray-200 bg-gray-50';
    }
  };

  return (
    <div className={`border rounded-lg p-4 ${getAdvisorColor(advisorType)}`}>
      <div className="flex items-center gap-2 mb-3">
        <Users size={20} className="text-gray-700" />
        <h3 className="font-bold text-lg text-gray-900">{advisorType}</h3>
      </div>
      <div className="space-y-3">
        <div>
          <p className="text-sm font-semibold text-gray-700">Key Concern</p>
          <p className="text-sm text-gray-600">{keyConcern}</p>
        </div>
        <div>
          <p className="text-sm font-semibold text-gray-700">Recommendation</p>
          <p className="text-sm text-gray-600">{recommendation}</p>
        </div>
        <div>
          <div className="flex items-start gap-2">
            <AlertCircle size={16} className="text-amber-600 flex-shrink-0 mt-0.5" />
            <div>
              <p className="text-sm font-semibold text-gray-700">Blind Spot</p>
              <p className="text-sm text-gray-600">{blindSpot}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
